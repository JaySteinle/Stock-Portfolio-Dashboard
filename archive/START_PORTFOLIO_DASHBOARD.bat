@echo off
title Stock Portfolio Dashboard

echo ========================================
echo         STOCK PORTFOLIO DASHBOARD
echo ========================================
echo.
echo 📊 Starting your investment tracker...
echo.

REM Navigate to the project directory
cd /d "C:\Users\jayst\OneDrive\Desktop\Stocks\Smart-Investment-Portfolio-Dashboard-python-excel-powerbi"

REM Check if we're in the right directory
if not exist "dashboard.py" (
    echo ❌ ERROR: Cannot find dashboard.py
    echo Please check if the project folder exists at:
    echo C:\Users\jayst\OneDrive\Desktop\Stocks\Smart-Investment-Portfolio-Dashboard-python-excel-powerbi
    pause
    exit /b 1
)

echo ✅ Found project files
echo.

REM Try to start the dashboard
echo 🚀 Launching web dashboard...
echo 🌐 Dashboard will open at: http://localhost:8501
echo.
echo 💡 Leave this window open while using the dashboard
echo 🛑 Close this window to stop the dashboard
echo.

REM Start the dashboard using simple py command
py -m streamlit run dashboard.py

REM If that fails, try with python.bat
if errorlevel 1 (
    echo.
    echo ⚠️  Trying python.bat fallback...
    python.bat -m streamlit run dashboard.py
)

REM If still fails, show error
if errorlevel 1 (
    echo.
    echo ❌ ERROR: Could not start dashboard
    echo.
    echo 🔧 Quick fixes:
    echo 1. Make sure Python is installed
    echo 2. Install required packages: pip install streamlit pandas yfinance plotly
    echo 3. Check the STARTUP_GUIDE.md file for detailed instructions
    echo.
)

pause