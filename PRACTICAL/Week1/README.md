# Week 1: Introduction to Gemini API Integration

## 1. Overview
In Week 1, we establish the foundational connection to Google's Gemini large language model using the modern `google-genai` Python SDK. The objective is to securely load API credentials using environment variables, initialize a client instance, submit a prompt, and retrieve and display the generated response.

---

## 2. Directory Structure & Files
```text
Week1/
├── .env                 # Environment file storing GEMINI_API_KEY (git-ignored)
├── main.py              # Script to initialize Gemini client and generate content
├── README.md            # Execution documentation and instructions
└── requirements.txt     # Python package dependencies
```

- **`main.py`**: Loads environment variables with `python-dotenv`, initializes `genai.Client`, and sends a prompt (`"Explain machine learning in simple words"`) to the `gemini-2.5-flash` model.
- **`.env`**: Contains sensitive API keys so they are not hardcoded into source code.
- **`requirements.txt`**: Specifies packages required to run the script.

---

## 3. Prerequisites & Setup

### A. Activate Python Virtual Environment
Open your terminal and activate your virtual environment:
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
Install the required packages:
```bash
pip install -r requirements.txt
```

### C. Configure Environment Variables
Create a file named `.env` inside the `Week1` directory (if not already present):
```env
GEMINI_API_KEY=your_gemini_api_key_here
```
> **Note:** Replace `your_gemini_api_key_here` with a valid Gemini API key from [Google AI Studio](https://aistudio.google.com/).

---

## 4. Execution Steps

Navigate to the `Week1` directory:
```bash
cd Week1
```

Run the script:
```bash
python main.py
```

Or run directly from the workspace root:
```bash
python Week1/main.py
```

---

## 5. Expected Output

Upon successful execution, the script contacts the Gemini API and outputs the generated response:

```text
LLM Response:
Imagine you want to teach a child to recognize a dog. You wouldn't give them a giant rulebook detailing ear shapes, snout lengths, and fur textures. Instead, you'd show them lots of pictures of dogs: "This is a dog. That's a dog. That's a cat (not a dog)." Eventually, their brain figures out the patterns on its own.

Machine learning works the same way for computers.

Instead of writing step-by-step code telling the computer how to solve a problem, you feed it lots of data (examples). The computer finds the patterns within that data and learns how to make decisions or predictions on its own.
```

---

## 6. Code Walkthrough (`main.py`)

1. **Environment Loading:**
   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()
   api_key = os.getenv("GEMINI_API_KEY")
   ```
   Reads `.env` securely without hardcoding credentials in code. Raises a `ValueError` if the key is missing.

2. **Client Initialization:**
   ```python
   from google import genai
   client = genai.Client(api_key=api_key)
   ```
   Instantiates the official Google GenAI client.

3. **Content Generation:**
   ```python
   response = client.models.generate_content(
       model="gemini-2.5-flash",
       contents="Explain machine learning in simple words"
   )
   print("\nLLM Response:")
   print(response.text)
   ```
   Dispatches the request to the `gemini-2.5-flash` model and prints the resulting text.

---

## 7. Troubleshooting

- **`ValueError: Gemini API key not found!`**: Ensure `.env` exists in `Week1/` with the key named `GEMINI_API_KEY` and contains no extra quotes or spaces.
- **`ModuleNotFoundError: No module named 'google'`**: Ensure your virtual environment is active and run `pip install -r requirements.txt`.
- **Network / SSL Errors**: Verify your internet connectivity and ensure your firewall does not block outgoing HTTPS requests to `generativelanguage.googleapis.com`.
