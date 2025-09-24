@echo off
echo ========================================
echo     STOCK TRACKER - CLEAN RESTART
echo ========================================

echo 📊 Updating all stock data...
python stock_tracker.py

echo.
echo 🚀 Starting web dashboard...
echo 🌐 Dashboard will open at: http://localhost:8501
echo 🛑 Press Ctrl+C to stop
echo.

python -m streamlit run dashboard.py

pause