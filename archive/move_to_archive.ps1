# Archive Cleanup Script
# Moves unnecessary files to archive folder

Write-Host "Moving unnecessary files to archive folder..." -ForegroundColor Yellow

# Python PATH fix files
$pythonFixes = @(
    "FIX_PYTHON_COMMANDS.bat",
    "FIX_PYTHON_PATH.ps1", 
    "FIX_PYTHON_PATH_SIMPLE.bat",
    "pip.bat",
    "python.bat",
    "simple_path_fix.ps1",
    "TEST_PYTHON_COMMANDS.bat"
)

# Documentation archive files
$docArchives = @(
    "ADD_STOCKS_FIX.md",
    "DASHBOARD_HEIGHT_EXPANSION.md", 
    "LEFT_PANEL_EXPANSION.md",
    "PYTHON_PATH_FIX_SUMMARY.md",
    "SIMPLE_COMMANDS.md",
    "WORKING_COMMANDS.md"
)

# Redundant startup scripts
$startupFiles = @(
    "setup.bat",
    "quick_start.bat", 
    "START_PORTFOLIO_DASHBOARD.bat"
)

# Development tools
$devTools = @(
    "check_portfolio.py",
    "diagnose.py",
    "restart_tracker.py"
)

# Maybe archive
$maybeArchive = @(
    "STARTUP_GUIDE.md",
    "USAGE_GUIDE.md"
)

# Move all file groups
$allFiles = $pythonFixes + $docArchives + $startupFiles + $devTools + $maybeArchive

$moved = 0
$notFound = 0

foreach ($file in $allFiles) {
    if (Test-Path $file) {
        try {
            Move-Item $file "archive\" -Force
            Write-Host "Moved: $file" -ForegroundColor Green
            $moved++
        } catch {
            Write-Host "Failed to move: $file" -ForegroundColor Red
        }
    } else {
        Write-Host "Not found: $file" -ForegroundColor DarkYellow
        $notFound++
    }
}

Write-Host "`nSummary:" -ForegroundColor Cyan
Write-Host "Files moved: $moved" -ForegroundColor Green
Write-Host "Files not found: $notFound" -ForegroundColor Yellow
Write-Host "All unnecessary files archived!" -ForegroundColor Green