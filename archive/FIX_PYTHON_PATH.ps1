# Permanent Python PATH Fix Script
# This adds Python to your system PATH permanently

Write-Host "🔧 FIXING PYTHON PATH PERMANENTLY" -ForegroundColor Cyan
Write-Host "=" * 50

# Python installation path
$PythonPath = "$env:LOCALAPPDATA\Programs\Python\Python313"
$PythonScriptsPath = "$env:LOCALAPPDATA\Programs\Python\Python313\Scripts"

Write-Host "📍 Python location: $PythonPath" -ForegroundColor Yellow

# Check if Python exists
if (-Not (Test-Path "$PythonPath\python.exe")) {
    Write-Host "❌ ERROR: Python not found at expected location" -ForegroundColor Red
    Write-Host "Please check your Python installation" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "✅ Python found" -ForegroundColor Green

# Get current user PATH
$CurrentPath = [Environment]::GetEnvironmentVariable("Path", "User")
Write-Host "📋 Current user PATH length: $($CurrentPath.Length) characters" -ForegroundColor Blue

# Check if Python is already in PATH
if ($CurrentPath -like "*$PythonPath*") {
    Write-Host "ℹ️  Python is already in user PATH" -ForegroundColor Blue
} else {
    Write-Host "📝 Adding Python to user PATH..." -ForegroundColor Yellow
    
    # Add Python paths to user PATH
    $NewPath = "$CurrentPath;$PythonPath;$PythonScriptsPath"
    [Environment]::SetEnvironmentVariable("Path", $NewPath, "User")
    
    Write-Host "✅ Python added to user PATH" -ForegroundColor Green
}

# Also disable Windows Store Python alias
Write-Host "🚫 Disabling Windows Store Python alias..." -ForegroundColor Yellow

$AppAliasesKey = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths"
if (Test-Path $AppAliasesKey) {
    # Remove python.exe and python3.exe aliases if they exist
    $PythonAliasPath = "$AppAliasesKey\python.exe"
    $Python3AliasPath = "$AppAliasesKey\python3.exe"
    
    if (Test-Path $PythonAliasPath) {
        Remove-Item $PythonAliasPath -Force -ErrorAction SilentlyContinue
        Write-Host "✅ Removed python.exe alias" -ForegroundColor Green
    }
    
    if (Test-Path $Python3AliasPath) {
        Remove-Item $Python3AliasPath -Force -ErrorAction SilentlyContinue
        Write-Host "✅ Removed python3.exe alias" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "🎉 PYTHON PATH FIX COMPLETE!" -ForegroundColor Green
Write-Host "=" * 50
Write-Host ""
Write-Host "📋 NEXT STEPS:" -ForegroundColor Cyan
Write-Host "1. ❗ RESTART PowerShell/VS Code for changes to take effect" -ForegroundColor Yellow
Write-Host "2. ❗ Close ALL terminal windows and reopen them" -ForegroundColor Yellow  
Write-Host "3. Test with: python --version" -ForegroundColor White
Write-Host "4. Then use: python -m streamlit run dashboard.py" -ForegroundColor White
Write-Host ""
Write-Host "⚠️  IMPORTANT: You MUST restart your terminals!" -ForegroundColor Red
Write-Host ""

Read-Host "Press Enter to exit (Remember to restart terminals!)"