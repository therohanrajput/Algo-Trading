# 📈 Algorithmic Trading & Quantitative Analysis Practice

Welcome to the **Algo-Trading** repository. This workspace is dedicated to mastering the core fundamentals of Python and applying them to quantitative finance, financial data analysis, and algorithmic trading strategy development.

---

## 🚀 Repository Structure

```filepath
├── 01_Python_Basics/
│   ├── 01_Basics.ipynb                        # Variables, basic data types, and built-in Python functions
│   └── 02_Operators_If_else_loops_modules.ipynb # Arithmetic/logical operators, control flow, loops, and modules
├── Projects/
│   └── 01_mini_project.py                      # Stock Data Entry and Analysis Tool
└── README.md                                  # Repository documentation
```

---

## 📂 Detailed Overview of Contents

### 1. 🐍 Python Basics (`01_Python_Basics/`)
An interactive Jupyter Notebook series designed to build a strong foundation in Python programming tailored for data analysis.
*   **`01_Basics.ipynb`**: Focuses on variables, core data structures (strings, numbers, lists), and basic console interaction.
*   **`02_Operators_If_else_loops_modules.ipynb`**: Covers logic gates, conditional branching (`if-elif-else`), iterative processes (`for` and `while` loops), and importing standard/third-party modules.

### 2. 💼 Financial Projects (`Projects/`)
Practical, real-world mini-projects that apply programming concepts to financial data.
*   **`01_mini_project.py` (Stock Data Entry & Analysis Tool)**:
    *   **Objective**: Automate stock tracking by taking manual price inputs over a trading week (5 working days).
    *   **Features**: Dynamic stock search, average price computation, and structured terminal reporting.

---

## 🛠 Setup & Installation

To run the interactive notebooks or scripts locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/therohanrajput/Algo-Trading.git
   cd Algo-Trading
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**:
   Ensure you have Jupyter installed to run the notebooks:
   ```bash
   pip install jupyter
   ```

4. **Launch Jupyter Notebooks**:
   ```bash
   jupyter notebook
   ```

---

## ⚙️ Future Roadmap
- [ ] **Data Acquisition**: Integrate Yahoo Finance (`yfinance`) and Alpha Vantage APIs to fetch real-time market data.
- [ ] **Technical Analysis Indicators**: Implement Moving Averages (SMA/EMA), Relative Strength Index (RSI), and MACD from scratch and using libraries like `pandas` and `ta`.
- [ ] **Backtesting Engine**: Develop an event-driven backtesting environment to test trading strategies against historical data.
- [ ] **API Integration & Execution**: Connect to paper-trading accounts (e.g., Alpaca API) for live-simulated order execution.
