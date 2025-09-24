@echo off
title Fix Python Commands

echo ========================================
echo       FIXING PYTHON COMMANDS
echo ========================================
echo.

REM Create alias for this session
echo 📝 Creating Python alias for this session...
doskey python="$env:LOCALAPPDATA\Programs\Python\Python313\python.exe" $*
doskey pip="$env:LOCALAPPDATA\Programs\Python\Python313\Scripts\pip.exe" $*

echo ✅ Python commands fixed for this session!
echo.
echo 🧪 Testing Python:
"%LOCALAPPDATA%\Programs\Python\Python313\python.exe" --version

echo.
echo 📊 Now you can use these commands:
echo    python --version
echo    python stock_tracker.py  
echo    python -m streamlit run dashboard.py
echo    pip install [package]
echo.
echo 💡 This fix only lasts for this command window.
echo    To make it permanent, use the PowerShell method.
echo.

cmd /k