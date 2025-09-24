"""
Complete Portfolio Restart Script
Restarts tracker with all symbols and launches dashboard
"""

import subprocess
import sys
import time
from stock_tracker import StockTracker

def restart_complete_tracker():
    """Restart tracker with all symbols"""
    print("🚀 RESTARTING COMPLETE STOCK TRACKER")
    print("=" * 50)
    
    # All symbols (ETFs + Individual stocks)
    all_symbols = ['SPY', 'QQQ', 'GLD', 'ARKK', 'TLT', 'AAPL', 'GOOGL', 'MSFT', 'TSLA', 'NVDA']
    
    print(f"📊 Tracking {len(all_symbols)} assets:")
    print("   ETFs: SPY, QQQ, GLD, ARKK, TLT")
    print("   Stocks: AAPL, GOOGL, MSFT, TSLA, NVDA")
    print()
    
    # Update all data
    tracker = StockTracker(all_symbols)
    success = tracker.run_update()
    
    if success:
        print("\n✅ All data updated successfully!")
        print("📊 Portfolio Summary:")
        
        # Show quick summary
        try:
            import pandas as pd
            df = pd.read_excel('Portfolio_Summary.xlsx')
            print(df[['Symbol', 'Current_Price', 'Daily_Return_Pct']].to_string(index=False))
        except Exception as e:
            print(f"Could not display summary: {e}")
        
        print("\n🌐 Web Dashboard: http://localhost:8501")
        print("📁 Excel Files: Updated with fresh data")
        print("📊 Power BI: Refresh your dashboard to see new data")
        
        return True
    else:
        print("\n❌ Failed to update data")
        return False

def main():
    """Main restart function"""
    restart_complete_tracker()

if __name__ == "__main__":
    main()