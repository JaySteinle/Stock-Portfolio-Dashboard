# 📊 Smart Investment Portfolio Dashboard — Power BI | Python | Excel

![Investment Dashboard](https://github.com/OkaforChukwuka/Smart-Investment-Portfolio-Dashboard-python-excel-powerbi/blob/main/Screenshot%202025-05-28%20112217.jpg?raw=true)

## 📌 Overview
This financial dashboard visualizes and monitors the performance of an investment portfolio comprising popular ETFs such as SPY, QQQ, GLD, and ARKK. The project uses Python for financial data ingestion, Excel for initial structuring, and Power BI for dashboard presentation and insights delivery.

---

## 💡 Project Objective
To create a smart dashboard for investment analysis, helping investors and analysts track asset weights, daily returns, cumulative performance, and historical price trends.

---

## 🛠️ Tools Used

| Tool        | Purpose                                        |
|-------------|------------------------------------------------|
| **Python**  | Pulling ETF data using APIs, data cleaning     |
| **Excel**   | Aggregation, structuring of price/return data |
| **Power BI**| Interactive visualization & portfolio tracking |

---

## 📈 Dashboard Features

- **Total Daily Return** and **Weight Metrics**
- **Top Performing ETF** indicator
- **Cumulative Returns Over Time** trendline
- **Price Trends by Year**
- **ETF Allocation Gauges**: SPY, QQQ, GLD, ARKK

---

## 📊 Key Insights

- SPY emerged as the **top performer** during the observed period
- Portfolio weight was dynamically balanced among 4+ ETFs
- Return volatility and consistency tracked across years
- Gauges and bar charts show **allocation vs performance** patterns

---

## 🧠 Skills Demonstrated

- Financial data analysis using Python (Pandas, yFinance, etc.)
- Time-series transformation and structuring in Excel
- Building dynamic, real-time dashboards in Power BI
- Investment KPIs, portfolio optimization visualization
- Interactive web dashboards with Streamlit
- Automated data pipelines and scheduling
- Real-time stock data integration

---

## 🚀 New Interactive Features

### 📊 Real-Time Stock Tracker (`stock_tracker.py`)
- **Automated Data Fetching**: Pulls live data from Yahoo Finance
- **Excel Integration**: Updates your existing Excel files with new data
- **Performance Metrics**: Calculates Sharpe ratio, max drawdown, volatility
- **Power BI Ready**: Exports consolidated data for Power BI consumption

### 🌐 Interactive Web Dashboard (`dashboard.py`)
- **Live Charts**: Interactive price trends and returns visualization
- **Real-Time Metrics**: Current performance indicators
- **Portfolio Insights**: Top gainers/losers analysis
- **Responsive Design**: Works on desktop and mobile

### ⏰ Automated Scheduler (`scheduler.py`)
- **Flexible Timing**: 15min, 30min, hourly, or daily updates
- **Background Processing**: Runs continuously in the background
- **Logging**: Comprehensive activity tracking
- **Error Handling**: Robust failure recovery

---

## 📋 Quick Setup

### Prerequisites
- Python 3.8+ installed
- Internet connection for data fetching

### 🚀 One-Click Setup
1. **Run the setup script**:
   ```bash
   setup.bat
   ```
   This will:
   - Install all required packages
   - Fetch initial stock data  
   - Launch the interactive dashboard

### 🔧 Manual Setup
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Fetch initial data**:
   ```bash
   python stock_tracker.py
   ```

3. **Launch dashboard**:
   ```bash
   streamlit run dashboard.py
   ```

4. **Start automated updates** (optional):
   ```bash
   python scheduler.py
   ```

---

## 📁 Project Structure

```
📂 Smart-Investment-Portfolio-Dashboard/
├── 📊 Excel Files/
│   ├── SPY.xlsx (Updated with live data)
│   ├── QQQ.xlsx (Updated with live data) 
│   ├── GLD.xlsx (Updated with live data)
│   ├── ARKK.xlsx (Updated with live data)
│   ├── TLT.xlsx (Updated with live data)
│   ├── Portfolio_Summary.xlsx (New)
│   └── Consolidated_Historical_Data.xlsx (New)
├── 🐍 Python Components/
│   ├── stock_tracker.py (Data fetching & Excel updates)
│   ├── dashboard.py (Interactive web interface)
│   ├── scheduler.py (Automated updates)
│   └── config.py (Configuration settings)
├── 📊 Power BI/
│   └── Investment Portfolio.pbix (Your existing dashboard)
└── 🔧 Setup/
    ├── requirements.txt (Python dependencies)
    └── setup.bat (One-click setup)

---

## 👨‍💼 About Me

I'm a data analyst with a growing interest in finance and investment analytics. This project combines real-world financial data with dynamic visualization to showcase my ability to work across tools and domains — transforming raw numbers into investment intelligence.

Let’s connect if you're looking for a **data analyst with business, finance, and technical fluency**.

---

## 📄 License

MIT License

---

## 📬 Contact

**Okafor Chukwuka A.**  
Email: [okaforchukwuka530@gmail.com]  
LinkedIn: [https://www.linkedin.com/in/okafor-chukwuka-6a7291307/]  
