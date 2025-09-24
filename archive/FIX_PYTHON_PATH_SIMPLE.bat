@echo off
title Fix Python PATH - Permanent Solution

echo ========================================
echo         FIX PYTHON PATH PERMANENTLY  
echo ========================================
echo.

echo 📝 Adding Python to your PATH...

REM Add Python to user PATH permanently
setx PATH "%PATH%;%LOCALAPPDATA%\Programs\Python\Python313;%LOCALAPPDATA%\Programs\Python\Python313\Scripts"

if errorlevel 1 (
    echo ❌ Failed to update PATH
    pause
    exit /b 1
)

echo ✅ Python added to PATH successfully!
echo.

echo 🎉 PATH FIX COMPLETE!
echo ⚠️  IMPORTANT: You must restart your terminal/VS Code
echo    for the changes to take effect.
echo.
echo After restarting, you can use:
echo   python --version
echo   python -m streamlit run dashboard.py  
echo   pip install [package]
echo.

echo 💡 If 'python' still doesn't work after restarting:
echo    1. Close ALL PowerShell/VS Code windows
echo    2. Reopen them fresh
echo    3. Try the manual disable method below
echo.

echo 🔧 Manual method (if needed):
echo    1. Windows Settings ^> Apps ^> Advanced app settings
echo    2. App execution aliases
echo    3. Turn OFF both Python toggles
echo.

pause