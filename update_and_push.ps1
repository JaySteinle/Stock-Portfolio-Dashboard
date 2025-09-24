# Portfolio Repository Update Script
# PowerShell version for VS Code terminal compatibility

Write-Host "📊 Updating Portfolio Repository..." -ForegroundColor Green
Write-Host "=======================================" -ForegroundColor Yellow

try {
    Write-Host "🔄 Fetching latest stock data..." -ForegroundColor Blue
    & py stock_tracker.py
    
    Write-Host "➕ Adding changes to git..." -ForegroundColor Blue
    & git add .
    
    Write-Host "💬 Creating commit..." -ForegroundColor Blue
    $today = Get-Date -Format "yyyy-MM-dd HH:mm"
    & git commit -m "📊 Portfolio update - $today"
    
    Write-Host "📤 Pushing to GitHub..." -ForegroundColor Blue
    & git push origin main
    
    Write-Host ""
    Write-Host "✅ Portfolio successfully pushed to GitHub!" -ForegroundColor Green
    Write-Host "🌐 View at: https://github.com/JaySteinle/Stock-Portfolio-Dashboard" -ForegroundColor Cyan
    Write-Host ""
    
} catch {
    Write-Host "❌ Error occurred: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "🔍 Check the terminal output above for details" -ForegroundColor Yellow
}

Write-Host "Press any key to continue..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")