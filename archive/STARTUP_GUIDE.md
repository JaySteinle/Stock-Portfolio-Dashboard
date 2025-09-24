# 🚀 Quick Start Guide - Fresh PC/VS Code Startup

## 📋 **After Restarting PC or Opening VS Code Fresh**

### 🎯 **Option 1: One-Click Start (Easiest)**
1. **Navigate to your project folder**:
   ```
   C:\Users\jayst\OneDrive\Desktop\Stocks\Smart-Investment-Portfolio-Dashboard-python-excel-powerbi
   ```

2. **Double-click one of these files**:
   - `quick_start.bat` (recommended)
   - `setup.bat` 

3. **Wait for dashboard to open** at: http://localhost:8501

---

### 🎯 **Option 2: From VS Code Terminal (FIXED)**
1. **Open VS Code**
2. **Open your project folder**: 
   - File → Open Folder → Select your stock tracker folder
3. **Open terminal** (Ctrl + `)
4. **Run one command** (use FULL Python path):
   ```powershell
   & "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe" -m streamlit run dashboard.py
   ```
5. **Visit**: http://localhost:8501

---

### 🎯 **Option 3: From Windows PowerShell (FIXED)**
1. **Open PowerShell** (Windows key + X → PowerShell)
2. **Navigate to folder**:
   ```powershell
   cd "C:\Users\jayst\OneDrive\Desktop\Stocks\Smart-Investment-Portfolio-Dashboard-python-excel-powerbi"
   ```
3. **Start dashboard** (use FULL Python path):
   ```powershell
   & "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe" -m streamlit run dashboard.py
   ```

---

## 📊 **What You'll See:**

### **Web Dashboard** (http://localhost:8501)
- 📈 Interactive stock charts
- 💹 Current prices and returns  
- 📊 Portfolio performance metrics
- 🔄 Update button for fresh data

### **Excel Files** (Always Available)
- `SPY.xlsx`, `QQQ.xlsx`, `GLD.xlsx`, `ARKK.xlsx`, `TLT.xlsx`
- `AAPL.xlsx`, `GOOGL.xlsx`, `MSFT.xlsx`, `TSLA.xlsx`, `NVDA.xlsx`
- `Portfolio_Summary.xlsx` (overview of all stocks)

### **Power BI Dashboard**
- Open `Investment Portfolio.pbix` in Power BI Desktop
- Click "Refresh" to get latest data

---

## 🔧 **Troubleshooting:**

### **If Python command doesn't work:**
```powershell
# Use full path
& "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe" -m streamlit run dashboard.py
```

### **If you get "Python not found":**
1. **Check Python installation**: Windows key → type "Python"
2. **Reinstall if needed**: Download from python.org
3. **Make sure "Add to PATH" is checked during install**

### **If packages are missing:**
```powershell
pip install pandas yfinance streamlit plotly openpyxl
```

---

## ⚡ **Quick Commands Reference:**

```bash
# View current portfolio (text format)
python -c "import pandas as pd; df = pd.read_excel('Portfolio_Summary.xlsx'); print(df[['Symbol', 'Current_Price', 'Daily_Return_Pct']].to_string(index=False))"

# Update all stock data
python stock_tracker.py

# Start web dashboard  
python -m streamlit run dashboard.py

# Add new stocks
python add_stocks.py AAPL GOOGL MSFT

# Run diagnostics
python diagnose.py
```

---

## 🎯 **Bookmark These:**

### **Dashboard URL:** http://localhost:8501
### **Project Folder:** 
```
C:\Users\jayst\OneDrive\Desktop\Stocks\Smart-Investment-Portfolio-Dashboard-python-excel-powerbi
```

---

## 📱 **Mobile Access:**
When dashboard is running, you can also access from phone/tablet on same network:
**http://192.168.1.64:8501** (or your network IP)

---

## 💡 **Pro Tips:**

1. **Bookmark the folder** for quick access
2. **Pin PowerShell to taskbar** for quick terminal access  
3. **Create desktop shortcut** to `quick_start.bat`
4. **Keep VS Code workspace** saved for this project
5. **The Excel files work offline** - no internet needed to view existing data

Your portfolio is always just one click away! 🚀📈