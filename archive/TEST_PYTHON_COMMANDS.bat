@echo off
title Test Python Commands

echo ========================================
echo        TESTING PYTHON COMMANDS
echo ========================================
echo.

echo 🧪 Testing if Python works with simple commands...
echo.

echo 📍 Testing: python --version
python --version
if errorlevel 1 (
    echo ❌ 'python' command still not working
    echo.
    echo 🔧 Solutions:
    echo 1. Close ALL terminal windows and VS Code
    echo 2. Reopen VS Code fresh
    echo 3. Or disable Windows Store Python aliases:
    echo    Windows Settings ^> Apps ^> Advanced ^> App execution aliases
    echo    Turn OFF both Python toggles
    echo.
    goto :manual_disable
) else (
    echo ✅ Python command works!
)

echo.
echo 📍 Testing: pip --version  
pip --version
if errorlevel 1 (
    echo ⚠️  pip command needs fixing
) else (
    echo ✅ Pip command works!
)

echo.
echo 🚀 Testing dashboard startup...
echo 💡 This should start your stock tracker dashboard:
echo.

python -m streamlit run dashboard.py

goto :end

:manual_disable
echo.
echo 🔧 MANUAL FIX INSTRUCTIONS:
echo ================================
echo 1. Press Windows key + I
echo 2. Go to Apps
echo 3. Click "Advanced app settings"  
echo 4. Click "App execution aliases"
echo 5. Turn OFF "App Installer python.exe" 
echo 6. Turn OFF "App Installer python3.exe"
echo 7. Restart your terminal
echo.

:end
pause