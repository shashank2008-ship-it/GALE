# Week 2: Provider Abstraction (Gemini & Ollama) and Unit Testing

## 1. Overview
Week 2 introduces architectural design patterns for LLM applications. Instead of coupling application code to a single vendor, we implement an abstract provider layer (`LLMProvider`) supporting both:
1. **Hosted Cloud LLM:** Google Gemini (`gemini-3.5-flash-lite` / `gemini-2.5-flash`) via `google-genai`.
2. **Local Self-Hosted LLM:** Ollama (`llama3.2`) via local HTTP REST API (`http://localhost:11434/api/generate`).

Additionally, we implement decoupled unit tests using a `FakeProvider` pattern to test application logic deterministically without incurring API costs or requiring internet access.

---

## 2. Directory Structure & Files
```text
Week2/
├── .env                 # API keys for cloud providers (GEMINI_API_KEY)
├── llm_client.py        # Abstract base class and provider implementations
├── main.py              # Interactive CLI application
├── test_client.py       # Unit tests verifying client behavior with FakeProvider
├── requirements.txt     # Python dependencies
└── README.md            # Documentation and execution guide
```

- **`llm_client.py`**: Defines `LLMProvider` (ABC), `GeminiProvider`, `OllamaProvider`, and `LLMClient`. Includes fallback logic for Gemini model availability.
- **`main.py`**: Prompts the user to select either `gemini` or `ollama`, accepts an input question, and prints the generated response.
- **`test_client.py`**: Uses Python's `unittest` framework and a `FakeProvider` to verify `LLMClient.generate()` without external dependencies.

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
Ensure `Week2/.env` contains your Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### D. (Optional) Setup Ollama for Local Inference
If you wish to test local inference with Ollama:
1. Download and install [Ollama](https://ollama.com/).
2. Pull and start the Llama 3.2 model:
   ```bash
   ollama pull llama3.2
   ollama run llama3.2
   ```

---

## 4. Execution Steps

Navigate to the `Week2` directory:
```bash
cd Week2
```

### Option A: Run Unit Tests (No external API or network required)
Execute the unit tests with `unittest`:
```bash
python test_client.py
```
Or run with pytest:
```bash
pytest test_client.py
```

### Option B: Run Interactive Application
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
```

### B. Interactive Execution with Gemini (`main.py`)
```text
Choose provider (gemini/ollama): gemini
Enter your question: What is artificial intelligence?

LLM Response:
Artificial intelligence (AI) is a branch of computer science focused on creating systems capable of performing tasks that typically require human intelligence. These tasks include problem-solving, pattern recognition, learning from experience, and natural language understanding.
```

### C. Interactive Execution with Ollama (`main.py`)
```text
Choose provider (gemini/ollama): ollama
Enter your question: What is machine learning in one sentence?

LLM Response:
Machine learning is a subset of artificial intelligence where algorithms learn patterns from data to make predictions or decisions without being explicitly programmed.
```

---

## 6. Code Walkthrough

### 1. Abstract Provider Interface (`llm_client.py`)
```python
from abc import ABC, abstractmethod

class LLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass
```
Any provider must implement `generate(prompt)`.

### 2. Gemini Implementation
```python
class GeminiProvider(LLMProvider):
    def __init__(self, api_key, model="gemini-3.5-flash-lite"):
        self.model = model
        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt):
        # Generates content and includes fallback handling for transient 404/503 errors
```

### 3. Ollama Implementation
```python
class OllamaProvider(LLMProvider):
    def __init__(self, model="llama3.2"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):
        response = requests.post(self.url, json={"model": self.model, "prompt": prompt, "stream": False})
        return response.json()["response"]
```

### 4. Client Wrapper & Unit Test Mocking
```python
class LLMClient:
    def __init__(self, provider: LLMProvider):
        self.provider = provider

    def generate(self, prompt: str) -> str:
        return self.provider.generate(prompt)
```
In `test_client.py`, `FakeProvider` implements `generate(prompt)` returning `"AI stands for Artificial Intelligence."`, allowing `LLMClient` to be thoroughly tested in CI/CD without making external network calls.

---

## 7. Troubleshooting
- **`ValueError: Gemini API key not found in .env`**: Check that `.env` is present in `Week2/` and `GEMINI_API_KEY` is set.
- **`requests.exceptions.ConnectionError: ... Connection refused (Ollama)`**: Ensure Ollama is running (`ollama serve`) on `localhost:11434`.
- **`ModuleNotFoundError: No module named 'llm_client'`**: Make sure you run `python test_client.py` from within the `Week2` directory or ensure `PYTHONPATH` includes `Week2`.
