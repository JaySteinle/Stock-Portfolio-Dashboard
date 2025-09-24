# 🔧 WORKING MANUAL COMMANDS - Method 3 FIXED

## ✅ **VERIFIED WORKING COMMANDS**

### 📂 **Step 1: Navigate to Project Folder**
```powershell
cd "C:\Users\jayst\OneDrive\Desktop\Stocks\Smart-Investment-Portfolio-Dashboard-python-excel-powerbi"
```

### 🚀 **Step 2: Start Dashboard (WORKING COMMAND)**
```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe" -m streamlit run dashboard.py
```

**Dashboard will open at:** http://localhost:8502 (or 8501)

---

## 📋 **ALL WORKING COMMANDS:**

### 📊 **View Portfolio Status:**
```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe" check_portfolio.py
```

### 🔄 **Update Stock Data:**
```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe" stock_tracker.py
```

### ➕ **Add New Stocks:**
```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe" add_stocks.py AAPL MSFT GOOGL
```

### 🔍 **Run Diagnostics:**
```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe" diagnose.py
```

### 📈 **Quick Portfolio View:**
```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe" -c "import pandas as pd; df = pd.read_excel('Portfolio_Summary.xlsx'); print(df[['Symbol', 'Current_Price', 'Daily_Return_Pct']].to_string(index=False))"
```

---

## 🎯 **COPY-PASTE READY COMMANDS:**

**For VS Code Terminal or PowerShell:**

```powershell
# Navigate to project
cd "C:\Users\jayst\OneDrive\Desktop\Stocks\Smart-Investment-Portfolio-Dashboard-python-excel-powerbi"

# Start dashboard
& "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe" -m streamlit run dashboard.py

# Alternative: Check status first
& "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe" check_portfolio.py
```

---

## 💡 **Why This Works:**

- **Full Python Path**: Uses complete path to Python executable
- **PowerShell Syntax**: `& "$env:..."` is proper PowerShell execution
- **No PATH Issues**: Bypasses Windows Store Python redirect

---

## 🚨 **If Dashboard Doesn't Open:**

1. **Check the terminal output** for the URL (might be 8501, 8502, etc.)
2. **Manually visit:** http://localhost:8501 or http://localhost:8502
3. **Check if another dashboard is running** (close other terminals)

---

## ✅ **TESTED AND VERIFIED:**

✅ Dashboard starts successfully  
✅ Portfolio data loads correctly  
✅ All 10 stocks tracked (SPY, QQQ, GLD, ARKK, TLT, AAPL, GOOGL, MSFT, TSLA, NVDA)  
✅ Interactive charts work  
✅ Real-time data updates available  

**Method 3 is now WORKING! 🚀**