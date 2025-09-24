@echo off
echo 📊 Starting Interactive Stock Portfolio Dashboard...
echo ===============================================

REM Change to the portfolio directory
cd /d "C:\Users\jayst\OneDrive\Desktop\Stocks\Smart-Investment-Portfolio-Dashboard-python-excel-powerbi"

REM Check if portfolio data exists, if not update it first
if not exist "Portfolio_Summary.xlsx" (
    echo 🔄 No portfolio data found. Fetching latest stock data...
    py stock_tracker.py
    echo.
)

REM Start the dashboard
echo 🚀 Launching portfolio dashboard...
echo 🌐 Dashboard will open in your browser automatically
echo 📊 URL: http://localhost:8504
echo.
echo 💡 TIP: Keep this window open while using the dashboard
echo ❌ To stop the dashboard, close this window or press Ctrl+C
echo.

py -m streamlit run dashboard.py

pause