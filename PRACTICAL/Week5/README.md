# Week 5: Token Economics, Capacity Planning & Budgeting

## 1. Overview
Week 5 provides a quantitative framework for **LLM Token Economics and Production Capacity Planning**. Before building an LLM-powered application, engineering teams must evaluate:
- Expected daily and monthly API costs based on user request volume.
- Throughput and rate limits: Requests Per Minute (RPM) and Tokens Per Minute (TPM).
- Safety buffer margins to accommodate traffic bursts and peak hours.
- Automated budget checks ensuring workloads stay within allocated financial and quota constraints.

---

## 2. Directory Structure & Files
```text
Week5/
├── .env                 # Workload assumptions, limits, and budget parameters
├── budget.py            # FeatureBudget calculation logic and report generator
├── test_budget.py       # Unit tests verifying economic models and edge cases
├── requirements.txt     # Python dependencies (python-dotenv)
└── README.md            # Documentation and formulas
```

- **`budget.py`**: Reads configuration via `.env`, computes token volumes, daily/monthly costs, peak RPM/TPM with safety margins, and outputs a formatted assessment.
- **`test_budget.py`**: Unit tests verifying cost estimations, capacity threshold logic, and budget failures.

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
Ensure `Week5/.env` reflects your workload parameters:
```env
INPUT_PRICE_PER_MILLION=0.30
OUTPUT_PRICE_PER_MILLION=1.20
REQUESTS_PER_DAY=2000
AVG_INPUT_TOKENS=1200
AVG_OUTPUT_TOKENS=300
PEAK_REQUESTS_PER_MINUTE=30
RPM_LIMIT=60
TPM_LIMIT=100000
MONTHLY_BUDGET_USD=50
DAILY_BUDGET_USD=2
SAFETY_MARGIN_PERCENT=20
```

---

## 4. Execution Steps

Navigate to the `Week5` directory:
```bash
cd Week5
```

### Option A: Run Unit Tests
```bash
python test_budget.py
```
Or with `unittest`:
```bash
python -m unittest test_budget.py
```

### Option B: Run Token Economics Report
```bash
python budget.py
```

---

## 5. Expected Output

### A. Unit Tests Output (`test_budget.py`)
```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.002s

OK
```

### B. Token Economics Report Output (`budget.py`)
```text
TOKEN ECONOMICS REPORT
-----------------------------------
Input tokens/day:  2,400,000
Output tokens/day: 600,000
Total tokens/day:  3,000,000
Estimated daily cost:   $1.4400
Estimated monthly cost: $43.20
Peak RPM with margin: 36.0
Peak TPM with margin: 54000

CHECKS
RPM capacity: PASS
TPM capacity: PASS
Daily budget: PASS
Monthly budget: REVIEW

Recommendation: REVISE assumptions, limits, or design before build.
```

---

## 6. Mathematical Formulas

1. **Daily Token Consumption:**
   $$\text{Input Tokens/Day} = \text{Requests/Day} \times \text{Avg Input Tokens}$$
   $$\text{Output Tokens/Day} = \text{Requests/Day} \times \text{Avg Output Tokens}$$
   $$\text{Total Tokens/Day} = \text{Input Tokens/Day} + \text{Output Tokens/Day}$$

2. **Daily & Monthly Cost:**
   $$\text{Daily Cost (\$) } = \frac{(\text{Input Tokens/Day} \times P_{\text{in}}) + (\text{Output Tokens/Day} \times P_{\text{out}})}{1,000,000}$$
   $$\text{Monthly Cost (\$) } = \text{Daily Cost} \times 30$$

3. **Peak Traffic with Safety Margin ($M$):**
   $$M = 1 + \frac{\text{Safety Margin \%}}{100}$$
   $$\text{Peak RPM}_{\text{with margin}} = \text{Peak Requests/Minute} \times M$$
   $$\text{Peak TPM}_{\text{with margin}} = \text{Peak Requests/Minute} \times (\text{Avg Input} + \text{Avg Output}) \times M$$

4. **Threshold Verification:**
   - **RPM Check:** $\text{Peak RPM}_{\text{with margin}} \le \text{RPM Limit}$
   - **TPM Check:** $\text{Peak TPM}_{\text{with margin}} \le \text{TPM Limit}$
   - **Daily Budget Check:** $\text{Daily Cost} \times M \le \text{Daily Budget USD}$
   - **Monthly Budget Check:** $\text{Monthly Cost} \times M \le \text{Monthly Budget USD}$

> In the sample run above, $\text{Monthly Cost with Margin} = \$43.20 \times 1.20 = \$51.84$. Since this exceeds the $\$50.00$ monthly budget, the check correctly flags `Monthly budget: REVIEW`.

---

## 7. Troubleshooting
- **`ValueError: Usage assumptions cannot be negative.`**: Verify that all parameters in `.env` are positive numbers.
- **`ZeroDivisionError` or missing keys**: Ensure `.env` exists in `Week5/` and contains all required variables with numeric values.
