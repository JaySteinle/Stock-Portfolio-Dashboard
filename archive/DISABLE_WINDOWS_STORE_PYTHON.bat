@echo off
title Disable Windows Store Python Alias

echo ========================================
echo    DISABLE WINDOWS STORE PYTHON ALIAS
echo ========================================
echo.

echo 🎯 This will disable the Windows Store Python redirect
echo    so you can use the real Python installation
echo.

echo 📝 Instructions to disable manually:
echo 1. Press Windows key + I (Settings)
echo 2. Go to Apps ^> Advanced app settings
echo 3. Click "App execution aliases"  
echo 4. Turn OFF the toggle for "App Installer python.exe"
echo 5. Turn OFF the toggle for "App Installer python3.exe"
echo.

echo ⚠️  OR run the PowerShell script: FIX_PYTHON_PATH.ps1
echo.

pause

echo 🚀 Opening Windows Settings for you...
start ms-settings:appsfeatures-app

echo.
echo Navigate to: Advanced app settings ^> App execution aliases
echo Turn OFF both Python toggles
echo.

pause