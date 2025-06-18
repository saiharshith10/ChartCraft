# 📊 ChartCraft

**ChartCraft** is an Excel data visualization tool that reads a multi-sheet Excel workbook and auto-generates simple plots for each sheet. It detects whether each sheet contains categorical or numerical data and produces appropriate graphs.

---

## 🎯 Features

- Reads `.xlsx` files with multiple sheets
- Automatically detects:
  - Categorical columns → 📋 Count plot
  - Numerical columns → 📈 Histogram
- Skips empty sheets
- Uses `seaborn` and `matplotlib` for visual styling

---

## 🧰 Tech Stack

- Python 3.x
- Pandas
- Seaborn
- Matplotlib
- Jupyter Notebook (for exploratory version)

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/saiharshith10/ChartCraft.git
cd ChartCraft
