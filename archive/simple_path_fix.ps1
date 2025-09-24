# Simple Python PATH Fix
Write-Host "🔧 FIXING PYTHON PATH..." -ForegroundColor Cyan

$PythonDir = "$env:LOCALAPPDATA\Programs\Python\Python313"
$PythonScripts = "$PythonDir\Scripts"

# Get current user PATH
$CurrentPath = [Environment]::GetEnvironmentVariable("Path", "User")

# Add Python to PATH if not already there
if ($CurrentPath -notlike "*$PythonDir*") {
    Write-Host "📝 Adding Python to PATH..." -ForegroundColor Yellow
    $NewPath = "$CurrentPath;$PythonDir;$PythonScripts"
    [Environment]::SetEnvironmentVariable("Path", $NewPath, "User")
    Write-Host "✅ Python added to PATH" -ForegroundColor Green
} else {
    Write-Host "ℹ️  Python already in PATH" -ForegroundColor Blue
}

Write-Host ""
Write-Host "🎉 PATH UPDATED!" -ForegroundColor Green
Write-Host "⚠️  RESTART your terminal to use 'python' command" -ForegroundColor Red
Write-Host ""
Write-Host "After restarting terminal, you can use:" -ForegroundColor Cyan
Write-Host "  python --version" -ForegroundColor White
Write-Host "  python -m streamlit run dashboard.py" -ForegroundColor White
Write-Host ""

Read-Host "Press Enter to continue"