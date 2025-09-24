# Interactive Stock Tracker Setup Script
# PowerShell version for better Windows compatibility

Write-Host "========================================"
Write-Host "   Interactive Stock Tracker Setup"  
Write-Host "========================================" -ForegroundColor Cyan

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "❌ ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python from https://python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Install required packages
Write-Host ""
Write-Host "📦 Installing required packages..." -ForegroundColor Yellow
try {
    pip install -r requirements.txt
    Write-Host "✅ Packages installed successfully" -ForegroundColor Green
}
catch {
    Write-Host "❌ Failed to install packages" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Run initial data fetch
Write-Host ""
Write-Host "📊 Fetching initial stock data..." -ForegroundColor Yellow
try {
    python stock_tracker.py
    Write-Host "✅ Initial data fetched successfully" -ForegroundColor Green
}
catch {
    Write-Host "⚠️  Warning: Initial data fetch failed, but continuing..." -ForegroundColor Yellow
}

# Start the dashboard
Write-Host ""
Write-Host "🚀 Starting interactive dashboard..." -ForegroundColor Cyan
Write-Host "🌐 The dashboard will open in your web browser" -ForegroundColor Green
Write-Host "🛑 Press Ctrl+C to stop the dashboard" -ForegroundColor Yellow
Write-Host ""

try {
    streamlit run dashboard.py
}
catch {
    Write-Host "❌ Failed to start dashboard" -ForegroundColor Red
    Write-Host "Please check that Streamlit is installed correctly" -ForegroundColor Yellow
}

Read-Host "Press Enter to exit"