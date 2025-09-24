@echo off
echo 📊 Updating Portfolio Repository...
echo =======================================

REM Update stock data first
echo 🔄 Fetching latest stock data...
py stock_tracker.py

REM Add all changes
echo ➕ Adding changes to git...
git add .

REM Create commit with timestamp
echo 💬 Creating commit...
for /f "tokens=1-3 delims=/ " %%a in ('date /t') do set today=%%c-%%a-%%b
git commit -m "📊 Portfolio update - %today%"

REM Push to GitHub
echo 📤 Pushing to GitHub...
git push origin main

echo.
echo ✅ Portfolio successfully pushed to GitHub!
echo 🌐 View at: https://github.com/JaySteinle/Stock-Portfolio-Dashboard
echo.
pause