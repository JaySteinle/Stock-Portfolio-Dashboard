# Stock Portfolio Dashboard Launcher
# PowerShell version for maximum compatibility

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "         STOCK PORTFOLIO DASHBOARD" -ForegroundColor Cyan  
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Set project directory
$ProjectDir = "C:\Users\jayst\OneDrive\Desktop\Stocks\Smart-Investment-Portfolio-Dashboard-python-excel-powerbi"

Write-Host "📂 Navigating to project folder..." -ForegroundColor Yellow
Set-Location $ProjectDir

# Check if files exist
if (-Not (Test-Path "dashboard.py")) {
    Write-Host "❌ ERROR: Cannot find dashboard.py" -ForegroundColor Red
    Write-Host "Please check if the project folder exists at:" -ForegroundColor Yellow
    Write-Host $ProjectDir -ForegroundColor Gray
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "✅ Found project files" -ForegroundColor Green
Write-Host ""

# Show current portfolio data if available
if (Test-Path "Portfolio_Summary.xlsx") {
    Write-Host "📊 Current Portfolio Status:" -ForegroundColor Cyan
    try {
        python -c "import pandas as pd; df = pd.read_excel('Portfolio_Summary.xlsx'); print(df[['Symbol', 'Current_Price', 'Daily_Return_Pct']].to_string(index=False))"
        Write-Host ""
    } catch {
        Write-Host "⚠️  Portfolio data available in Excel files" -ForegroundColor Yellow
    }
}

Write-Host "🚀 Launching web dashboard..." -ForegroundColor Green
Write-Host "🌐 Dashboard will open at: http://localhost:8501" -ForegroundColor Cyan
Write-Host ""
Write-Host "💡 Leave this window open while using the dashboard" -ForegroundColor Yellow
Write-Host "🛑 Press Ctrl+C to stop the dashboard" -ForegroundColor Yellow
Write-Host ""

# Try to start dashboard
try {
    python -m streamlit run dashboard.py
} catch {
    Write-Host ""
    Write-Host "⚠️  Trying alternative Python path..." -ForegroundColor Yellow
    try {
        & "$env:LOCALAPPDATA\Programs\Python\Python313\python.exe" -m streamlit run dashboard.py
    } catch {
        Write-Host ""
        Write-Host "❌ ERROR: Could not start dashboard" -ForegroundColor Red
        Write-Host ""
        Write-Host "🔧 Quick fixes:" -ForegroundColor Cyan
        Write-Host "1. Make sure Python is installed" -ForegroundColor White
        Write-Host "2. Install packages: pip install streamlit pandas yfinance plotly" -ForegroundColor White
        Write-Host "3. Check the STARTUP_GUIDE.md file for help" -ForegroundColor White
        Write-Host ""
    }
}

Read-Host "Press Enter to exit"