# Create Desktop Shortcut for Portfolio Dashboard
# This script creates a shortcut on the desktop

Write-Host "Creating Desktop Shortcut for Portfolio Dashboard..." -ForegroundColor Green

# Get desktop path
$desktopPath = [System.Environment]::GetFolderPath('Desktop')
$shortcutPath = Join-Path $desktopPath "Stock Portfolio Dashboard.lnk"

# Get current directory (portfolio folder)
$portfolioPath = Get-Location
$batchFilePath = Join-Path $portfolioPath "Launch_Portfolio_Dashboard.bat"

# Create shortcut
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($shortcutPath)

# Set shortcut properties
$Shortcut.TargetPath = $batchFilePath
$Shortcut.WorkingDirectory = $portfolioPath
$Shortcut.Description = "Launch Interactive Stock Portfolio Dashboard"
$Shortcut.IconLocation = "C:\Windows\System32\shell32.dll,15"  # Chart icon

# Save the shortcut
$Shortcut.Save()

Write-Host "Desktop shortcut created successfully!" -ForegroundColor Green
Write-Host "Location: $shortcutPath" -ForegroundColor Yellow
Write-Host "Double-click the shortcut to launch your portfolio dashboard!" -ForegroundColor Cyan

# Also create a quick launcher in the project folder
$quickLaunchPath = Join-Path $portfolioPath "Launch Dashboard.lnk"
$QuickShortcut = $WshShell.CreateShortcut($quickLaunchPath)
$QuickShortcut.TargetPath = $batchFilePath
$QuickShortcut.WorkingDirectory = $portfolioPath
$QuickShortcut.Description = "Quick Launch Portfolio Dashboard"
$QuickShortcut.IconLocation = "C:\Windows\System32\shell32.dll,15"
$QuickShortcut.Save()

Write-Host "Also created quick launcher in project folder!" -ForegroundColor Green