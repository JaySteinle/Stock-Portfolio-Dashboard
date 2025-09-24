"""
Quick Portfolio Status Viewer
Shows your current portfolio without starting the web dashboard
"""

import pandas as pd
import os
from datetime import datetime

def show_portfolio_status():
    """Display current portfolio status"""
    print("📊 STOCK PORTFOLIO STATUS")
    print("=" * 50)
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    try:
        # Load portfolio summary
        if os.path.exists('Portfolio_Summary.xlsx'):
            df = pd.read_excel('Portfolio_Summary.xlsx')
            
            print("💼 CURRENT HOLDINGS:")
            print("-" * 30)
            
            # Display key metrics
            for _, row in df.iterrows():
                symbol = row['Symbol']
                price = row['Current_Price']
                change = row['Daily_Return_Pct']
                
                # Color coding for returns
                if change > 0:
                    change_str = f"+{change:.2f}% ⬆️"
                elif change < 0:
                    change_str = f"{change:.2f}% ⬇️"
                else:
                    change_str = f"{change:.2f}% ➡️"
                
                print(f"{symbol:6} | ${price:8.2f} | {change_str}")
            
            print()
            
            # Portfolio summary
            avg_return = df['Daily_Return_Pct'].mean()
            total_symbols = len(df)
            positive_returns = (df['Daily_Return_Pct'] > 0).sum()
            
            print("📈 PORTFOLIO SUMMARY:")
            print("-" * 30)
            print(f"Total Assets: {total_symbols}")
            print(f"Positive Today: {positive_returns}/{total_symbols}")
            print(f"Average Return: {avg_return:.2f}%")
            
            if avg_return > 0:
                print("🟢 Portfolio is UP today!")
            elif avg_return < 0:
                print("🔴 Portfolio is DOWN today")
            else:
                print("🟡 Portfolio is FLAT today")
                
        else:
            print("❌ No portfolio data found.")
            print("Run 'python stock_tracker.py' to fetch data.")
            
    except Exception as e:
        print(f"❌ Error reading portfolio data: {str(e)}")
    
    print()
    print("🔧 QUICK ACTIONS:")
    print("-" * 30)
    print("📊 Start web dashboard: python -m streamlit run dashboard.py")
    print("🔄 Update data: python stock_tracker.py") 
    print("➕ Add stocks: python add_stocks.py SYMBOL")
    print("🌐 Web URL: http://localhost:8501")

def show_file_status():
    """Show which data files are available"""
    print("\n📁 DATA FILES STATUS:")
    print("-" * 30)
    
    # Check individual stock files
    symbols = ['SPY', 'QQQ', 'GLD', 'ARKK', 'TLT', 'AAPL', 'GOOGL', 'MSFT', 'TSLA', 'NVDA']
    
    for symbol in symbols:
        filename = f"{symbol}.xlsx"
        if os.path.exists(filename):
            try:
                df = pd.read_excel(filename)
                print(f"✅ {filename}: {len(df)} records")
            except:
                print(f"⚠️  {filename}: Corrupted")
        else:
            print(f"❌ {filename}: Missing")
    
    # Check summary files
    summary_files = ['Portfolio_Summary.xlsx', 'Consolidated_Historical_Data.xlsx', 'Investment Portfolio.pbix']
    for filename in summary_files:
        if os.path.exists(filename):
            print(f"✅ {filename}: Available")
        else:
            print(f"❌ {filename}: Missing")

if __name__ == "__main__":
    show_portfolio_status()
    show_file_status()