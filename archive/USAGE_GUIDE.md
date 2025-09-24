# 📊 Interactive Stock Tracker - Usage Guide

## 🎯 Overview
This enhanced stock tracker combines Python automation with Power BI visualization to create a comprehensive investment dashboard that updates automatically with real-time data.

## 🚀 Getting Started

### Option 1: Quick Setup (Recommended)
Run the setup script in PowerShell:
```powershell
.\setup.ps1
```
Or in Command Prompt:
```cmd
setup.bat
```

### Option 2: Manual Setup
1. Install Python packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Run initial data fetch:
   ```bash
   python stock_tracker.py
   ```

3. Launch web dashboard:
   ```bash
   streamlit run dashboard.py
   ```

## 📋 Components Overview

### 1. 📈 Stock Tracker (`stock_tracker.py`)
**Purpose**: Fetches live stock data and updates Excel files

**Key Features**:
- Pulls data from Yahoo Finance API
- Updates existing Excel files with new data sheets
- Calculates performance metrics (Sharpe ratio, volatility, max drawdown)
- Creates consolidated files for Power BI integration

**Usage**:
```python
from stock_tracker import StockTracker

# Initialize with default symbols (SPY, QQQ, GLD, ARKK, TLT)
tracker = StockTracker()

# Or with custom symbols
tracker = StockTracker(['AAPL', 'GOOGL', 'TSLA'])

# Run update
tracker.run_update()
```

### 2. 🌐 Interactive Dashboard (`dashboard.py`)
**Purpose**: Web-based interface for real-time monitoring

**Features**:
- Interactive price and returns charts
- Real-time performance metrics
- Portfolio insights and analysis
- Mobile-responsive design

**Access**: Open http://localhost:8501 after running `streamlit run dashboard.py`

**Controls**:
- **Update Data Button**: Refreshes all stock data
- **Symbol Selector**: Choose which ETFs to display
- **Expandable Sections**: Volume analysis and additional charts

### 3. ⏰ Automated Scheduler (`scheduler.py`)
**Purpose**: Automatically updates data at specified intervals

**Update Frequencies**:
- Every 15 minutes
- Every 30 minutes  
- Every hour (recommended)
- Every 2 hours
- Daily at 9:30 AM (market open)

**Usage**:
```bash
python scheduler.py
```
Then select your preferred update frequency.

### 4. ⚙️ Configuration (`config.py`)
**Purpose**: Central configuration for all settings

**Key Settings**:
- Default symbols to track
- Portfolio weights
- Risk-free rate for calculations
- File paths and naming conventions
- Chart colors and styling

## 📊 Power BI Integration

### Updated Data Files
The Python components create/update these files for Power BI:

1. **Individual ETF Files**: `SPY.xlsx`, `QQQ.xlsx`, etc.
   - `Historical_Data` sheet: Price, volume, returns data
   - `Summary_Stats` sheet: Key metrics and ratios
   - `Performance_Metrics` sheet: Returns across time periods

2. **Portfolio_Summary.xlsx**: Current snapshot of all ETFs
   - Current prices and daily returns
   - Volume and cumulative performance
   - Last updated timestamps

3. **Consolidated_Historical_Data.xlsx**: All historical data combined
   - Perfect for Power BI time-series analysis
   - Includes calculated fields for advanced analytics

### Power BI Refresh Process
1. **Automatic**: If you have Power BI Pro/Premium, set up scheduled refresh
2. **Manual**: Click "Refresh" in Power BI Desktop
3. **Real-time**: Use Power BI streaming datasets (advanced)

## 💡 Usage Scenarios

### Scenario 1: Daily Monitoring
1. Start the scheduler with hourly updates:
   ```bash
   python scheduler.py
   ```
2. Keep the web dashboard open for real-time monitoring
3. Check Power BI dashboard for detailed analysis

### Scenario 2: Research & Analysis  
1. Update data manually for latest information:
   ```bash
   python stock_tracker.py
   ```
2. Use web dashboard for initial screening
3. Deep dive in Power BI for comprehensive analysis

### Scenario 3: Presentation Mode
1. Ensure data is current
2. Use Power BI for executive presentations
3. Use web dashboard for interactive Q&A sessions

## 🔧 Customization Options

### Adding New Symbols
Edit `config.py`:
```python
DEFAULT_SYMBOLS = ['SPY', 'QQQ', 'GLD', 'ARKK', 'TLT', 'YOUR_SYMBOL']
```

### Changing Portfolio Weights
Update in `config.py`:
```python
PORTFOLIO_WEIGHTS = {
    'SPY': 0.30,   # Increase S&P 500 weight
    'QQQ': 0.25,   # NASDAQ 100
    'GLD': 0.15,   # Reduce Gold weight
    'ARKK': 0.15,  # Innovation ETF  
    'TLT': 0.15    # Long-term Treasury
}
```

### Custom Time Periods
Modify in `stock_tracker.py`:
```python
# Fetch different periods
tracker.fetch_current_data(period="2y")  # 2 years
tracker.fetch_current_data(period="5y")  # 5 years
tracker.fetch_current_data(period="max") # Maximum available
```

## 🚨 Troubleshooting

### Common Issues

**1. Python not found**
- Install Python from python.org
- Add Python to system PATH
- Restart command prompt/PowerShell

**2. Package installation fails**
- Try: `pip install --upgrade pip`
- Use: `pip install --user -r requirements.txt`

**3. Data fetch errors**
- Check internet connection
- Verify symbol names are correct
- Yahoo Finance may have temporary outages

**4. Dashboard won't start**
- Ensure Streamlit is installed: `pip install streamlit`
- Check port 8501 isn't in use
- Try: `streamlit run dashboard.py --server.port 8502`

**5. Excel files not updating**
- Check file permissions
- Close Excel files before running updates
- Verify openpyxl is installed

### Performance Tips

1. **Reduce Update Frequency**: Use hourly instead of 15-minute updates
2. **Limit Symbols**: Track only ETFs you actively monitor  
3. **Close Unused Applications**: Especially Excel when updating files
4. **Use SSD Storage**: For faster file I/O operations

## 📈 Advanced Features

### Custom Indicators
Add technical indicators in `stock_tracker.py`:
```python
# RSI calculation example
def calculate_rsi(prices, window=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

# Add to your data processing
hist['RSI'] = calculate_rsi(hist['Close'])
```

### Database Integration
For high-frequency updates, consider SQLite:
```python
import sqlite3

# Store data in database instead of Excel
conn = sqlite3.connect('stock_data.db')
hist.to_sql('stock_prices', conn, if_exists='append')
```

### API Integration
Connect to other data sources:
```python
# Alpha Vantage, IEX Cloud, etc.
import requests

def fetch_alternative_data(symbol):
    # Your API integration here
    pass
```

## 🔒 Security & Best Practices

1. **API Keys**: Store in environment variables, not code
2. **Data Backup**: Regularly backup Excel files
3. **Version Control**: Use Git for code changes
4. **Error Handling**: Monitor logs for issues
5. **Resource Usage**: Don't over-fetch data unnecessarily

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review error logs (`stock_tracker.log`)
3. Verify all dependencies are installed
4. Check Yahoo Finance service status

---

**Happy Tracking! 📊📈**