# Week 3: Observability, Usage Logging (MongoDB), Latency & Cost Tracking

## 1. Overview
In Week 3, we build production-grade **Observability and Telemetry** into the LLM client:
- **Token Usage Extraction:** Captures prompt (input) tokens and candidate (output) tokens from provider metadata.
- **Latency Measurement:** Measures round-trip API latency with millisecond precision using `time.perf_counter()`.
- **Cost Calculation:** Computes financial cost dynamically using configurable per-million token pricing rates.
- **Centralized Database Logging:** Persists structured execution logs into a MongoDB collection (`llm_monitoring.api_usage`).
- **Resilient Retry Logic:** Implements exponential backoff retries for transient HTTP errors (e.g., 429 rate limits, 503 service unavailable, timeouts).

---

## 2. Directory Structure & Files
```text
Week3/
├── .env                 # API keys, MongoDB URI, and pricing configurations
├── llm_client.py        # Enhanced LLM client with telemetry, metrics & retries
├── usage_logger.py      # MongoDB client logger for storing call records
├── main.py              # CLI entry point demonstrating logging and error handling
├── test_client.py       # Unit tests validating usage logging and token tracking
├── requirements.txt     # Python package dependencies
└── README.md            # Documentation and execution guide
```

- **`usage_logger.py`**: Connects to MongoDB, validates connection via ping, and logs records with timestamp and retry handling.
- **`llm_client.py`**: Standardizes outputs into `LLMResult`, calculates USD cost, and logs execution details.
- **`test_client.py`**: Verifies with `FakeLogger` and `FakeProvider` that tokens and metrics are tracked correctly without requiring a live MongoDB instance.

---

## 3. Prerequisites & Setup

### A. Activate Python Virtual Environment
- **Windows (PowerShell):**
  ```powershell
  ..\Scripts\Activate.ps1
  ```
- **Windows (Command Prompt):**
  ```cmd
  ..\Scripts\activate.bat
  ```
- **Linux / macOS:**
  ```bash
  source ../bin/activate
  ```

### B. Install Dependencies
```bash
pip install -r requirements.txt
```

### C. Configure `.env`
Ensure `Week3/.env` is configured with your Gemini key and MongoDB connection string:
```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash
GEMINI_INPUT_PRICE_PER_MILLION=0.15
GEMINI_OUTPUT_PRICE_PER_MILLION=0.60
MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority
```
> **Note:** If you do not have MongoDB Atlas running, you can run a local MongoDB container via Docker (`docker run -d -p 27017:27017 mongo`) or test the client logic using the unit tests in `test_client.py`.

---

## 4. Execution Steps

Navigate to the `Week3` directory:
```bash
cd Week3
```

### Option A: Run Unit Tests (No MongoDB or API required)
```bash
python test_client.py
```
Or with pytest:
```bash
pytest test_client.py
```

### Option B: Run Full Observability Pipeline
```bash
python main.py
```

---

## 5. Expected Output

### A. Unit Tests Output (`test_client.py`)
```text
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
Latency: 0.0 ms
Input tokens: 5
Output tokens: 8
Estimated cost (USD): 0.0
```

### B. Full Pipeline Output (`main.py`)
```text
Choose provider (gemini/ollama): gemini
Enter your question: Explain the role of attention mechanism in transformers in two sentences.

Latency: 842.15 ms
Input tokens: 23
Output tokens: 46
Estimated cost (USD): 3.105e-05
Usage details saved to MongoDB.

LLM Response:
The attention mechanism allows transformer models to dynamically weight the relevance of different words in an input sequence regardless of their positional distance. This enables the model to capture complex contextual relationships and dependencies more effectively than traditional sequential architectures.
```

---

## 6. MongoDB Document Schema

Each API invocation is stored in the `llm_monitoring.api_usage` collection with the following structure:

```json
{
  "_id": "673f4b238a9e4b1029c7d1e1",
  "provider": "Gemini",
  "model": "gemini-2.5-flash",
  "input_tokens": 23,
  "output_tokens": 46,
  "total_tokens": 69,
  "latency_ms": 842.15,
  "estimated_cost_usd": 0.00003105,
  "cost_type": "estimated_hosted_api_cost",
  "status": "success",
  "attempts": 1,
  "timestamp": "2026-11-20T10:30:15.123Z"
}
```

If an invocation fails after retries, the record is saved with `status: "failed"` and the error details:
```json
{
  "provider": "Gemini",
  "status": "failed",
  "attempts": 3,
  "error": "ResourceExhausted: 429 Resource has been exhausted (quota limit reached).",
  "latency_ms": 7210.45,
  "timestamp": "2026-11-20T10:35:00.000Z"
}
```

---

## 7. Key Features Explained

1. **Dataclass `LLMResult`**:
   Standardizes vendor-specific token structures into a single consistent contract (`text`, `input_tokens`, `output_tokens`).
2. **Cost Calculation**:
   $$\text{Cost (USD)} = \frac{(\text{Input Tokens} \times P_{\text{input}}) + (\text{Output Tokens} \times P_{\text{output}})}{1,000,000}$$
3. **Exponential Backoff Retry**:
   Catches retryable HTTP status codes (`408`, `429`, `500`, `502`, `503`, `504`) and connection timeouts, retrying up to 3 attempts with delays of $2^0 = 1\text{s}$, $2^1 = 2\text{s}$, etc.
4. **Graceful Teardown**:
   The `main.py` script wraps execution in a `try...finally` block to ensure `usage_logger.close()` cleanly closes the MongoDB connection pool.

---

## 8. Troubleshooting
- **`ValueError: MONGODB_URI not found in .env`**: Supply a valid MongoDB connection string in `Week3/.env`.
- **`ServerSelectionTimeoutError`**: Ensure your IP address is whitelisted in MongoDB Atlas Network Access rules (e.g., "Allow access from anywhere" for development).
- **Transient Rate Limit (429)**: The client will automatically display:
  `Temporary error. Retry 1 of 2 in 1 seconds.`
