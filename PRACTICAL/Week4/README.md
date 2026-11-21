# Week 4: Tokenizer Comparison Across Languages & Algorithms

## 1. Overview
Week 4 focuses on **Tokenization Fundamentals** and analyzes how different subword tokenization algorithms split text across different human languages and writing systems.

We evaluate three major tokenizers:
1. **BPE (Byte Pair Encoding):** Using the `gpt2` vocabulary.
2. **WordPiece:** Using `bert-base-multilingual-cased` (Multilingual BERT).
3. **SentencePiece (Unigram / BPE):** Using `xlm-roberta-base` (XLM-R).

We test these tokenizers on three languages representing Latin and Indic scripts:
- **English:** Latin alphabet (`Artificial intelligence is changing the world.`)
- **Telugu:** Telugu script (`కృత్రిమ మేధస్సు ప్రపంచాన్ని మారుస్తోంది.`)
- **Hindi:** Devanagari script (`कृत्रिम बुद्धिमत्ता दुनिया को बदल रही है।`)

---

## 2. Directory Structure & Files
```text
Week4/
├── tokenizer_comparison.py   # Tokenization comparison script
├── requirements.txt          # Python dependencies (transformers, sentencepiece)
└── README.md                 # Documentation and analysis
```

- **`tokenizer_comparison.py`**: Loads the pre-trained tokenizers via Hugging Face `transformers`, encodes each text sample, and compares token representations, token IDs, and total token counts.
- **`requirements.txt`**: Specifies `transformers` and `sentencepiece`.

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

---

## 4. Execution Steps

Navigate to the `Week4` directory:
```bash
cd Week4
```

Run the comparison script:
```bash
python tokenizer_comparison.py
```

> **Tip for Offline Environments:** If working offline or in a restricted network sandbox with cached models, set:
> - **PowerShell:** `$env:HF_HUB_OFFLINE="1"; python tokenizer_comparison.py`
> - **Bash:** `HF_HUB_OFFLINE=1 python tokenizer_comparison.py`

---

## 5. Expected Output

```text
Loading BPE - GPT-2...
Loading WordPiece - Multilingual BERT...
Loading SentencePiece - XLM-R...

===========================================================================
LANGUAGE: English
INPUT TEXT: Artificial intelligence is changing the world.
===========================================================================

BPE - GPT-2
Tokens     : ['Art', 'ificial', 'Ġintelligence', 'Ġis', 'Ġchanging', 'Ġthe', 'Ġworld', '.']
Token IDs  : [8001, 9542, 4430, 318, 5609, 262, 995, 13]
Token count: 8

WordPiece - Multilingual BERT
Tokens     : ['[CLS]', 'Arti', '##ficial', 'intelligence', 'is', 'changing', 'the', 'world', '.', '[SEP]']
Token IDs  : [101, 90841, 69229, 30151, 10124, 43068, 10105, 11356, 119, 102]
Token count: 10

SentencePiece - XLM-R
Tokens     : ['<s>', ' Artificial', ' ', 'intelligence', ' is', ' changing', ' the', ' world', '.', '</s>']
Token IDs  : [0, 231996, 6, 130687, 83, 151134, 70, 8999, 5, 2]
Token count: 10

===========================================================================
LANGUAGE: Telugu
INPUT TEXT: కృత్రిమ మేధస్సు ప్రపంచాన్ని మారుస్తోంది.
===========================================================================

BPE - GPT-2
Tokens     : ['à', '°', 'ķ', 'à', '±', 'ĥ', 'à', '°', '¤', 'à', '±', 'į', 'à', '°', '°', 'à', '°', '¿', 'à', '°', '®', 'Ġ', 'à', '°', '®', 'à', '±', 'ĩ', 'à', '°', '§', 'à', '°', '¸', 'à', '±', 'į', 'à', '°', '¸', 'à', '±', 'ģ', 'Ġ', 'à', '°', 'ª', 'à', '±', 'į', 'à', '°', '°', 'à', '°', 'ª', 'à', '°', 'Ĥ', 'à', '°', 'ļ', 'à', '°', '¾', 'à', '°', '¨', 'à', '±', 'į', 'à', '°', '¨', 'à', '°', '¿', 'Ġ', 'à', '°', '®', 'à', '°', '¾', 'à', '°', '°', 'à', '±', 'ģ', 'à', '°', '¸', 'à', '±', 'į', 'à', '°', '¤', 'à', '±', 'ĭ', 'à', '°', 'Ĥ', 'à', '°', '¦', 'à', '°', '¿', '.']
Token IDs  : [156, 108, 243, 156, 109, 225, 156, 108, 97, 156, 109, 235, 156, 108, 108, 156, 108, 123, 156, 108, 106, 220, 156, 108, 106, 156, 109, 229, 156, 108, 100, 156, 108, 116, 156, 109, 235, 156, 108, 116, 156, 109, 223, 220, 156, 108, 103, 156, 109, 235, 156, 108, 108, 156, 108, 103, 156, 108, 224, 156, 108, 248, 156, 108, 122, 156, 108, 101, 156, 109, 235, 156, 108, 101, 156, 108, 123, 220, 156, 108, 106, 156, 108, 122, 156, 108, 108, 156, 109, 223, 156, 108, 116, 156, 109, 235, 156, 108, 97, 156, 109, 233, 156, 108, 224, 156, 108, 99, 156, 108, 123, 13]
Token count: 112

WordPiece - Multilingual BERT
Tokens     : ['[CLS]', 'క', '##ృ', '##త్రి', '##మ', 'మ', '##ే', '##ధ', '##స్', '##సు', 'ప్రపంచ', '##ాన్ని', 'మ', '##ారు', '##స్', '##తోంది', '.', '[SEP]']
Token IDs  : [101, 1201, 111339, 88046, 24696, 1224, 17729, 99288, 15370, 39179, 94504, 23769, 1224, 27374, 15370, 68450, 119, 102]
Token count: 18

SentencePiece - XLM-R
Tokens     : ['<s>', ' ', 'కృత', '్రి', 'మ', ' మే', 'ధ', 'స్సు', ' ప్రపంచ', 'ాన్ని', ' మారు', 'స్తోంది', '.', '</s>']
Token IDs  : [0, 6, 151424, 91445, 3071, 22290, 11600, 129461, 86457, 6258, 169610, 104528, 5, 2]
Token count: 14

===========================================================================
LANGUAGE: Hindi
INPUT TEXT: कृत्रिम बुद्धिमत्ता दुनिया को बदल रही है।
===========================================================================

BPE - GPT-2
Tokens     : ['à¤', 'ķ', 'à¥', 'ĥ', 'à¤', '¤', 'à¥', 'į', 'à¤', '°', 'à¤', '¿', 'à¤', '®', 'Ġà¤', '¬', 'à¥', 'ģ', 'à¤', '¦', 'à¥', 'į', 'à¤', '§', 'à¤', '¿', 'à¤', '®', 'à¤', '¤', 'à¥', 'į', 'à¤', '¤', 'à¤¾', 'Ġà¤', '¦', 'à¥', 'ģ', 'à¤', '¨', 'à¤', '¿', 'à¤', '¯', 'à¤¾', 'Ġà¤', 'ķ', 'à¥', 'ĭ', 'Ġà¤', '¬', 'à¤', '¦', 'à¤', '²', 'Ġà¤', '°', 'à¤', '¹', 'à¥', 'Ģ', 'Ġà¤', '¹', 'à¥', 'Ī', 'à¥', '¤']
Token IDs  : [11976, 243, 24231, 225, 11976, 97, 24231, 235, 11976, 108, 11976, 123, 11976, 106, 28225, 105, 24231, 223, 11976, 99, 24231, 235, 11976, 100, 11976, 123, 11976, 106, 11976, 97, 24231, 235, 11976, 97, 48077, 28225, 99, 24231, 223, 11976, 101, 11976, 123, 11976, 107, 48077, 28225, 243, 24231, 233, 28225, 105, 11976, 99, 11976, 110, 28225, 108, 11976, 117, 24231, 222, 28225, 117, 24231, 230, 24231, 97]
Token count: 68

WordPiece - Multilingual BERT
Tokens     : ['[CLS]', 'क', '##ृत', '##्र', '##िम', 'ब', '##ुद्ध', '##िम', '##त्ता', 'दुनिया', 'को', 'ब', '##दल', 'रही', 'है', '।', '[SEP]']
Token IDs  : [101, 865, 37500, 18321, 50419, 887, 48010, 50419, 94034, 83874, 11267, 887, 99989, 57203, 10569, 920, 102]
Token count: 17

SentencePiece - XLM-R
Tokens     : ['<s>', ' कृत', '्रि', 'म', ' बुद्धि', 'म', 'त्ता', ' दुनिया', ' को', ' बदल', ' रही', ' है', '।', '</s>']
Token IDs  : [0, 74707, 97885, 1920, 105202, 1920, 54297, 29405, 629, 14512, 8906, 460, 125, 2]
Token count: 14
```

---

## 6. Key Findings & Analysis

| Language | Word Count | GPT-2 (BPE) Tokens | mBERT (WordPiece) Tokens | XLM-R (SentencePiece) Tokens |
| :--- | :---: | :---: | :---: | :---: |
| **English** | 6 | **8** | 10 | 10 |
| **Telugu** | 4 | **112** (14x inflation!) | 18 | **14** |
| **Hindi** | 7 | **68** (9.7x inflation!) | 17 | **14** |

### Insights:
1. **The "Token Tax" on Non-Latin Scripts:**
   - GPT-2's vocabulary was trained overwhelmingly on English text. Non-ASCII Unicode characters (such as Telugu and Devanagari) fall back to individual raw UTF-8 bytes (`à`, `°`, `ķ`), causing massive token expansion.
   - 4 Telugu words require **112 tokens** in GPT-2 vs. only **14 tokens** in XLM-RoBERTa.
2. **Cost & Context Window Implications:**
   - Because LLM APIs charge per token and models have finite context windows, using a model with a poorly optimized tokenizer for Indic languages costs up to **10–14x more** for the exact same semantic content!
3. **Multilingual Tokenizers:**
   - XLM-RoBERTa (SentencePiece) and Multilingual BERT (WordPiece) include dedicated subwords and character matrices for Indic scripts, producing significantly more compact and semantically meaningful token sequences.
