@echo off
REM Quick setup script for the Interactive Stock Tracker
REM Run this to install dependencies and start the dashboard

echo ========================================
echo   Interactive Stock Tracker Setup
echo ========================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo ✅ Python found

REM Install required packages
echo.
echo 📦 Installing required packages...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install packages
    pause
    exit /b 1
)

echo ✅ Packages installed successfully

REM Run initial data fetch
echo.
echo 📊 Fetching initial stock data...
python stock_tracker.py

if errorlevel 1 (
    echo ⚠️  Warning: Initial data fetch failed, but continuing...
) else (
    echo ✅ Initial data fetched successfully
)

REM Start the dashboard
echo.
echo 🚀 Starting interactive dashboard...
echo 🌐 The dashboard will open in your web browser
echo 🛑 Press Ctrl+C to stop the dashboard

streamlit run dashboard.py

pause