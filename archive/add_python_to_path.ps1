# Python PATH Setup Script
# Run this in PowerShell as Administrator

Write-Host "🔍 Searching for Python 3.13 installation..." -ForegroundColor Yellow

# Common Python installation locations
$pythonPaths = @(
    "$env:LOCALAPPDATA\Programs\Python\Python313",
    "$env:LOCALAPPDATA\Programs\Python\Python313-32",
    "C:\Python313",
    "C:\Program Files\Python313",
    "C:\Program Files (x86)\Python313"
)

$foundPython = $null

foreach ($path in $pythonPaths) {
    if (Test-Path "$path\python.exe") {
        $foundPython = $path
        Write-Host "✅ Found Python at: $path" -ForegroundColor Green
        break
    }
}

if ($foundPython) {
    Write-Host "📝 Adding Python to PATH..." -ForegroundColor Yellow
    
    # Get current user PATH
    $currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
    
    # Paths to add
    $pythonExePath = $foundPython
    $pythonScriptsPath = "$foundPython\Scripts"
    
    # Check if already in PATH
    if ($currentPath -notlike "*$pythonExePath*") {
        $newPath = "$currentPath;$pythonExePath;$pythonScriptsPath"
        [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
        Write-Host "✅ Python added to PATH successfully!" -ForegroundColor Green
        Write-Host "🔄 Please restart PowerShell/VS Code to use the new PATH" -ForegroundColor Cyan
    } else {
        Write-Host "ℹ️  Python is already in PATH" -ForegroundColor Blue
    }
    
    Write-Host ""
    Write-Host "🧪 Testing Python installation:" -ForegroundColor Yellow
    & "$foundPython\python.exe" --version
    
} else {
    Write-Host "❌ Python 3.13 not found in common locations" -ForegroundColor Red
    Write-Host "Please check where Python is installed and add it manually" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "To find Python, try:" -ForegroundColor Cyan
    Write-Host "Get-ChildItem -Path C:\ -Name python.exe -Recurse -ErrorAction SilentlyContinue" -ForegroundColor Gray
}

Write-Host ""
Write-Host "After restarting PowerShell, test with:" -ForegroundColor Cyan
Write-Host "python --version" -ForegroundColor Gray
Write-Host "pip --version" -ForegroundColor Gray