"""
Stock Tracker Diagnostic Tool
Identifies and reports all issues with the system
"""

import os
import sys
import pandas as pd
from datetime import datetime

def check_python_environment():
    """Check Python setup"""
    print("🐍 PYTHON ENVIRONMENT CHECK")
    print("-" * 30)
    print(f"✅ Python Version: {sys.version}")
    
    # Check required packages
    required_packages = ['pandas', 'yfinance', 'streamlit', 'plotly', 'openpyxl', 'schedule']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}: Installed")
        except ImportError:
            print(f"❌ {package}: Missing")
            missing_packages.append(package)
    
    return len(missing_packages) == 0

def check_data_files():
    """Check if data files exist and are readable"""
    print("\n📁 DATA FILES CHECK")
    print("-" * 30)
    
    # Check for Excel files
    expected_symbols = ['SPY', 'QQQ', 'GLD', 'ARKK', 'TLT', 'AAPL', 'GOOGL', 'MSFT', 'TSLA', 'NVDA']
    missing_files = []
    corrupt_files = []
    
    for symbol in expected_symbols:
        filename = f"{symbol}.xlsx"
        if os.path.exists(filename):
            try:
                df = pd.read_excel(filename)
                print(f"✅ {filename}: {len(df)} records")
            except Exception as e:
                print(f"⚠️  {filename}: Corrupt ({str(e)})")
                corrupt_files.append(filename)
        else:
            print(f"❌ {filename}: Missing")
            missing_files.append(filename)
    
    # Check summary files
    summary_files = ['Portfolio_Summary.xlsx', 'Consolidated_Historical_Data.xlsx']
    for filename in summary_files:
        if os.path.exists(filename):
            try:
                df = pd.read_excel(filename)
                print(f"✅ {filename}: {len(df)} records")
            except Exception as e:
                print(f"⚠️  {filename}: Corrupt ({str(e)})")
        else:
            print(f"❌ {filename}: Missing")
    
    return len(missing_files) == 0 and len(corrupt_files) == 0

def check_configuration():
    """Check configuration files"""
    print("\n⚙️ CONFIGURATION CHECK")
    print("-" * 30)
    
    try:
        from config import Config
        print(f"✅ Config loaded")
        print(f"📊 Default symbols: {Config.DEFAULT_SYMBOLS}")
        print(f"🔄 Update frequency: {Config.UPDATE_FREQUENCY}")
        return True
    except Exception as e:
        print(f"❌ Config error: {str(e)}")
        return False

def check_stock_tracker():
    """Test stock tracker functionality"""
    print("\n📊 STOCK TRACKER CHECK")
    print("-" * 30)
    
    try:
        from stock_tracker import StockTracker
        print("✅ StockTracker class loaded")
        
        # Test with one symbol
        tracker = StockTracker(['SPY'])
        print("✅ StockTracker initialized")
        return True
    except Exception as e:
        print(f"❌ StockTracker error: {str(e)}")
        return False

def check_dashboard():
    """Check dashboard components"""
    print("\n🌐 DASHBOARD CHECK")
    print("-" * 30)
    
    try:
        import streamlit
        print(f"✅ Streamlit version: {streamlit.__version__}")
        
        # Check if dashboard.py exists and is readable
        if os.path.exists('dashboard.py'):
            print("✅ dashboard.py exists")
            with open('dashboard.py', 'r') as f:
                content = f.read()
                if 'use_container_width' in content:
                    print("⚠️  Dashboard contains deprecated 'use_container_width'")
                else:
                    print("✅ Dashboard syntax up to date")
        else:
            print("❌ dashboard.py missing")
            
        return True
    except Exception as e:
        print(f"❌ Dashboard error: {str(e)}")
        return False

def check_network():
    """Check network connectivity for data fetching"""
    print("\n🌐 NETWORK CHECK")
    print("-" * 30)
    
    try:
        import yfinance as yf
        
        # Test fetching one symbol
        ticker = yf.Ticker("SPY")
        info = ticker.history(period="1d")
        
        if not info.empty:
            print("✅ Yahoo Finance API accessible")
            print(f"📊 Test data: {len(info)} records fetched")
            return True
        else:
            print("⚠️  Yahoo Finance returned empty data")
            return False
            
    except Exception as e:
        print(f"❌ Network error: {str(e)}")
        return False

def generate_solutions():
    """Generate solutions for common problems"""
    print("\n🔧 QUICK FIXES")
    print("-" * 30)
    
    print("To fix missing packages:")
    print("  pip install pandas yfinance streamlit plotly openpyxl schedule")
    print()
    print("To regenerate missing data files:")
    print("  python stock_tracker.py")
    print()
    print("To start dashboard:")
    print("  python -m streamlit run dashboard.py")
    print()
    print("To add new stocks:")
    print("  python add_stocks.py SYMBOL1 SYMBOL2")
    print()
    print("Dashboard URL:")
    print("  http://localhost:8501")

def main():
    """Run complete diagnostic"""
    print("🔍 STOCK TRACKER DIAGNOSTIC REPORT")
    print("=" * 50)
    print(f"📅 Timestamp: {datetime.now()}")
    print(f"📂 Working Directory: {os.getcwd()}")
    print()
    
    checks = [
        check_python_environment(),
        check_configuration(),
        check_stock_tracker(),
        check_data_files(),
        check_dashboard(),
        check_network()
    ]
    
    passed_checks = sum(checks)
    total_checks = len(checks)
    
    print(f"\n📋 SUMMARY")
    print("-" * 30)
    print(f"✅ Passed: {passed_checks}/{total_checks} checks")
    
    if passed_checks == total_checks:
        print("🎉 All systems operational!")
        print("🚀 Your stock tracker is ready to use")
    else:
        print("⚠️  Some issues detected")
        print("📋 See solutions below")
    
    generate_solutions()

if __name__ == "__main__":
    main()