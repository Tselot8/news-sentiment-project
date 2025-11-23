# Predicting Price Moves with News Sentiment

This repo contains analysis for the Nova Financial Insights Week-1 challenge.

---

## 📁 Project Structure
```
project-root/
│
├── src/ # Main project source code
├── tests/ # Unit tests (pytest)
├── requirements.txt # Python dependencies
├── .github/workflows/ # CI workflows (GitHub Actions)
│ └── unittests.yml # Automated testing pipeline
└── README.md # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository
```
git clone https://github.com/Tselot8/news-sentiment-project.git
cd news-sentiment-project
```
### 2. Create a virtual environment 
```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
### 3. Install dependencies
```
pip install -r requirements.txt
```

## 🧪 Running Tests

This project uses pytest for unit testing.

Run the full test suite with:
```
pytest -q
```
## 🔄 Continuous Integration (CI)

GitHub Actions automatically runs tests on:
- Every push to: main, task-1, task-2, task-3
- Every Pull Request to main

The pipeline installs dependencies and executes the test suite to ensure everything passes.

You can find the workflow in:
```
.github/workflows/unittests.yml
```

## 📊 Features

### Task 1: Git & Environment Setup

- Repository created and linked to a local environment using SSH
- Clear directory structure for code, tests, data, and reports
- Feature branches for tasks (task-1, task-2) with pull requests to merge into main
- Python virtual environment with all dependencies installed
- Automated testing pipeline configured for CI

### Task 2: Quantitative Stock Analysis

- Loaded and prepared six stock CSV files (AAPL, AMZN, GOOG, META, MSFT, NVDA)
- Normalized column names and forward/back-filled missing data
- Calculated technical indicators using Finta (SMA 20/50, EMA 20, RSI 14, MACD)
   Note: TA-Lib could not be installed due to compilation issues, so Finta was used as an alternative
- Computed financial metrics using PyNance (Sharpe Ratio, Annualized Return, Annualized Volatility, Max Drawdown)
- Generated visualizations:
    - Close Price + Moving Averages
    - RSI(14) with overbought/oversold thresholds
    - MACD, Signal line, and Histogram
- Saved cleaned and enriched datasets as .parquet for future modeling or dashboard integration

## 📦 Deliverables Ready

- GitHub repository with branches task-1 and task-2
- Python environment set up and fully reproducible
- Cleaned and enriched datasets for six stocks
- Visualizations for technical indicators
- Quantitative metrics table per stock