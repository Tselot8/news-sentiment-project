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

- Clean and modular Python code
- Automated testing pipeline
- Organized project structure
- Easy to extend with new tasks or features