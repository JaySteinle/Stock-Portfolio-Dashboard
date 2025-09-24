"""
Interactive Stock Tracker - Python Component
Fetches real-time stock data and updates Excel files for Power BI integration
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import json
from typing import Dict, List, Tuple
from config import Config

class StockTracker:
    def __init__(self, symbols: List[str] = None):
        """Initialize the Stock Tracker with all configured symbols (ETFs + Individual Stocks)"""
        self.symbols = symbols or Config.DEFAULT_SYMBOLS
        self.data_folder = os.path.dirname(os.path.abspath(__file__))
        
    def fetch_current_data(self, period: str = "1y") -> Dict[str, pd.DataFrame]:
        """Fetch current stock data for all symbols"""
        print("📊 Fetching current stock data...")
        stock_data = {}
        
        for symbol in self.symbols:
            try:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(period=period)
                
                # Calculate additional metrics
                hist['Daily_Return'] = hist['Close'].pct_change()
                hist['Cumulative_Return'] = (1 + hist['Daily_Return']).cumprod() - 1
                hist['Volume_MA'] = hist['Volume'].rolling(window=20).mean()
                hist['Price_MA_20'] = hist['Close'].rolling(window=20).mean()
                hist['Price_MA_50'] = hist['Close'].rolling(window=50).mean()
                
                # Reset index to make Date a column
                hist.reset_index(inplace=True)
                hist['Date'] = hist['Date'].dt.date
                
                stock_data[symbol] = hist
                print(f"✅ {symbol}: {len(hist)} records fetched")
                
            except Exception as e:
                print(f"❌ Error fetching {symbol}: {str(e)}")
                
        return stock_data
    
    def update_excel_files(self, stock_data: Dict[str, pd.DataFrame]):
        """Update Excel files with new data"""
        print("📝 Updating Excel files...")
        
        for symbol, data in stock_data.items():
            excel_file = os.path.join(self.data_folder, f"{symbol}.xlsx")
            
            try:
                # Create Excel writer with multiple sheets
                with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
                    # Main data sheet
                    data.to_excel(writer, sheet_name='Historical_Data', index=False)
                    
                    # Summary statistics sheet
                    summary = self.create_summary_stats(data, symbol)
                    summary.to_excel(writer, sheet_name='Summary_Stats', index=False)
                    
                    # Performance metrics sheet
                    performance = self.create_performance_metrics(data, symbol)
                    performance.to_excel(writer, sheet_name='Performance_Metrics', index=False)
                
                print(f"✅ Updated {excel_file}")
                
            except Exception as e:
                print(f"❌ Error updating {symbol}.xlsx: {str(e)}")
    
    def create_summary_stats(self, data: pd.DataFrame, symbol: str) -> pd.DataFrame:
        """Create summary statistics for the stock"""
        latest_price = data['Close'].iloc[-1] if not data.empty else 0
        latest_date = data['Date'].iloc[-1] if not data.empty else datetime.now().date()
        
        stats = {
            'Metric': [
                'Current Price',
                'Daily Change (%)',
                'Volume',
                'Market Cap (Est.)',
                '52W High',
                '52W Low',
                'Avg Daily Return (%)',
                'Volatility (%)',
                'Sharpe Ratio (Est.)',
                'Max Drawdown (%)'
            ],
            'Value': [
                round(latest_price, 2),
                round(data['Daily_Return'].iloc[-1] * 100, 2) if not data.empty else 0,
                int(data['Volume'].iloc[-1]) if not data.empty else 0,
                'N/A',  # Would need market cap data
                round(data['High'].max(), 2) if not data.empty else 0,
                round(data['Low'].min(), 2) if not data.empty else 0,
                round(data['Daily_Return'].mean() * 100, 4) if not data.empty else 0,
                round(data['Daily_Return'].std() * 100 * np.sqrt(252), 2) if not data.empty else 0,
                round(self.calculate_sharpe_ratio(data['Daily_Return']), 3) if not data.empty else 0,
                round(self.calculate_max_drawdown(data['Cumulative_Return']) * 100, 2) if not data.empty else 0
            ],
            'Last_Updated': [latest_date] * 10
        }
        
        return pd.DataFrame(stats)
    
    def create_performance_metrics(self, data: pd.DataFrame, symbol: str) -> pd.DataFrame:
        """Create performance metrics over different time periods"""
        if data.empty:
            return pd.DataFrame()
            
        periods = {
            '1D': 1,
            '1W': 7,
            '1M': 30,
            '3M': 90,
            '6M': 180,
            '1Y': 365
        }
        
        performance_data = []
        
        for period_name, days in periods.items():
            if len(data) >= days:
                start_price = data['Close'].iloc[-days]
                end_price = data['Close'].iloc[-1]
                return_pct = ((end_price - start_price) / start_price) * 100
                
                performance_data.append({
                    'Period': period_name,
                    'Return_Percent': round(return_pct, 2),
                    'Start_Price': round(start_price, 2),
                    'End_Price': round(end_price, 2),
                    'Days': days
                })
        
        return pd.DataFrame(performance_data)
    
    @staticmethod
    def calculate_sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.02) -> float:
        """Calculate Sharpe ratio"""
        if returns.empty or returns.std() == 0:
            return 0
        excess_return = returns.mean() - (risk_free_rate / 252)  # Daily risk-free rate
        return excess_return / returns.std() * np.sqrt(252)
    
    @staticmethod
    def calculate_max_drawdown(cumulative_returns: pd.Series) -> float:
        """Calculate maximum drawdown"""
        if cumulative_returns.empty:
            return 0
        peak = cumulative_returns.expanding().max()
        drawdown = (cumulative_returns - peak) / (1 + peak)
        return drawdown.min()
    
    def create_portfolio_summary(self, stock_data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
        """Create portfolio-wide summary"""
        portfolio_data = []
        
        for symbol, data in stock_data.items():
            if not data.empty:
                latest_data = data.iloc[-1]
                portfolio_data.append({
                    'Symbol': symbol,
                    'Current_Price': round(latest_data['Close'], 2),
                    'Daily_Return_Pct': round(latest_data['Daily_Return'] * 100, 2),
                    'Volume': int(latest_data['Volume']),
                    'Cumulative_Return_Pct': round(latest_data['Cumulative_Return'] * 100, 2),
                    'MA_20': round(latest_data['Price_MA_20'], 2),
                    'MA_50': round(latest_data['Price_MA_50'], 2),
                    'Last_Updated': latest_data['Date']
                })
        
        return pd.DataFrame(portfolio_data)
    
    def export_for_powerbi(self, stock_data: Dict[str, pd.DataFrame]):
        """Export consolidated data for Power BI consumption"""
        print("🔄 Exporting data for Power BI...")
        
        # Create portfolio summary
        portfolio_summary = self.create_portfolio_summary(stock_data)
        portfolio_file = os.path.join(self.data_folder, "Portfolio_Summary.xlsx")
        portfolio_summary.to_excel(portfolio_file, index=False)
        
        # Create consolidated historical data
        all_historical = []
        for symbol, data in stock_data.items():
            data_copy = data.copy()
            data_copy['Symbol'] = symbol
            all_historical.append(data_copy)
        
        if all_historical:
            consolidated_data = pd.concat(all_historical, ignore_index=True)
            consolidated_file = os.path.join(self.data_folder, "Consolidated_Historical_Data.xlsx")
            consolidated_data.to_excel(consolidated_file, index=False)
            
        print("✅ Power BI export completed")
    
    def run_update(self):
        """Main method to run the complete update process"""
        print("🚀 Starting Stock Tracker Update...")
        print(f"📅 Timestamp: {datetime.now()}")
        print(f"📊 Tracking symbols: {', '.join(self.symbols)}")
        
        # Fetch current data
        stock_data = self.fetch_current_data()
        
        if stock_data:
            # Update individual Excel files
            self.update_excel_files(stock_data)
            
            # Export for Power BI
            self.export_for_powerbi(stock_data)
            
            print("✅ Stock tracker update completed successfully!")
            return True
        else:
            print("❌ No data fetched. Update failed.")
            return False


def main():
    """Main execution function"""
    # Initialize tracker with all configured symbols (ETFs + Stocks)
    tracker = StockTracker()  # Uses Config.DEFAULT_SYMBOLS
    
    # Run the update
    success = tracker.run_update()
    
    if success:
        print("\n🎉 Your Excel files are now updated and ready for Power BI!")
        print("📊 Next steps:")
        print("   1. Refresh your Power BI dashboard")
        print("   2. Check the new Portfolio_Summary.xlsx file")
        print("   3. Review Consolidated_Historical_Data.xlsx for trends")
    
    return success


if __name__ == "__main__":
    main()