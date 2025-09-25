# 🐍 **Python Comments Guide**

## 📝 **Types of Comments in Python:**

### 1. **# Single Line Comments**
```python
# This is a single line comment
print("Hello World")  # Comment at end of line

# You can use multiple single line comments
# to create multi-line explanations
# like this block here
```

### 2. **""" Multi-Line Comments (Docstrings) """**
```python
"""
This is a multi-line comment using triple quotes.
It's often used for documentation at the top of files,
functions, and classes.
"""

def my_function():
    """
    This is a function docstring.
    It explains what the function does.
    """
    pass
```

### 3. **''' Alternative Multi-Line Comments '''**
```python
'''
You can also use single quotes for multi-line comments.
Both work the same way.
'''
```

---

## 🔧 **Commenting Best Practices:**

### ✅ **Good Comments:**
```python
# Calculate portfolio performance metrics
total_return = (current_value - initial_value) / initial_value

# API rate limit: 5 requests per minute
time.sleep(12)  # Wait 12 seconds between calls

def fetch_stock_data(symbol):
    """
    Fetch historical stock data from Yahoo Finance API.
    
    Args:
        symbol (str): Stock ticker symbol (e.g., 'AAPL', 'SPY')
    
    Returns:
        pd.DataFrame: Historical price data
    """
```

### ❌ **Avoid Over-Commenting:**
```python
# Bad: obvious comments
x = 5  # Set x to 5
y = x + 1  # Add 1 to x and store in y

# Good: explain WHY, not WHAT
portfolio_size = 5  # Limit to 5 stocks for diversification
risk_factor = portfolio_size + 1  # Extra buffer for volatility
```

---

## 📊 **Commenting Your Portfolio Code:**

### **Config File Example:**
```python
"""
Stock Portfolio Configuration
Manages symbols, settings, and API parameters for the portfolio tracker.
"""

# ETF Holdings - Exchange Traded Funds for diversification
ETF_SYMBOLS = [
    'SPY',   # S&P 500 - Large cap US stocks
    'QQQ',   # NASDAQ 100 - Technology heavy
    'GLD',   # Gold ETF - Inflation hedge
]

# Individual Stock Holdings - High growth potential
STOCK_SYMBOLS = [
    'AAPL',  # Apple - Technology leader
    'GOOGL', # Google - Search and cloud dominance
    'MSFT',  # Microsoft - Enterprise software
]

# API Configuration
DEFAULT_PERIOD = "1y"      # 1 year historical data
UPDATE_FREQUENCY = "1h"    # Refresh every hour
MAX_RETRIES = 3           # API retry attempts on failure
```

### **Function Documentation:**
```python
def calculate_portfolio_return(prices, weights):
    """
    Calculate weighted portfolio return based on individual stock returns.
    
    This function takes historical price data and portfolio weights
    to compute the overall portfolio performance metrics.
    
    Args:
        prices (dict): Dictionary of stock symbols to price DataFrames
        weights (dict): Portfolio allocation weights (must sum to 1.0)
    
    Returns:
        float: Portfolio return as decimal (0.15 = 15% return)
        
    Raises:
        ValueError: If weights don't sum to 1.0
        KeyError: If price data missing for any weighted symbol
    
    Example:
        >>> prices = {'AAPL': df_aapl, 'GOOGL': df_googl}
        >>> weights = {'AAPL': 0.6, 'GOOGL': 0.4}
        >>> return_pct = calculate_portfolio_return(prices, weights)
        >>> print(f"Portfolio returned {return_pct:.2%}")
    """
    # Input validation
    if abs(sum(weights.values()) - 1.0) > 0.001:  # Allow small floating point errors
        raise ValueError("Portfolio weights must sum to 1.0")
    
    # Calculate individual stock returns
    stock_returns = {}
    for symbol in weights.keys():
        if symbol not in prices:
            raise KeyError(f"Missing price data for {symbol}")
        
        # Get first and last prices for return calculation
        start_price = prices[symbol]['Close'].iloc[0]
        end_price = prices[symbol]['Close'].iloc[-1]
        stock_returns[symbol] = (end_price - start_price) / start_price
    
    # Calculate weighted portfolio return
    portfolio_return = sum(
        stock_returns[symbol] * weights[symbol] 
        for symbol in weights.keys()
    )
    
    return portfolio_return
```

---

## 🎯 **VS Code Comment Shortcuts:**

### **Keyboard Shortcuts:**
- **Ctrl + /** : Toggle single line comment
- **Alt + Shift + A** : Toggle block comment
- **Shift + Alt + Down** : Copy line down
- **Ctrl + Shift + K** : Delete line

### **Comment/Uncomment Multiple Lines:**
1. Select the lines you want to comment
2. Press **Ctrl + /** 
3. All selected lines get `#` added/removed

---

## 📋 **Comment Templates:**

### **File Header:**
```python
"""
Stock Portfolio Dashboard - Main Module
Author: Jay Steinle
Created: September 2025
Description: Interactive portfolio tracker with real-time data fetching,
            Streamlit dashboard, and Power BI integration.
"""
```

### **Function Template:**
```python
def function_name(param1, param2):
    """
    Brief description of what the function does.
    
    Args:
        param1 (type): Description of first parameter
        param2 (type): Description of second parameter
    
    Returns:
        return_type: Description of return value
    
    Raises:
        ExceptionType: When this exception occurs
    """
    # Implementation here
    pass
```

### **Class Template:**
```python
class StockTracker:
    """
    Main class for tracking stock portfolio performance.
    
    This class handles data fetching, processing, and storage
    for a collection of stock and ETF symbols.
    
    Attributes:
        symbols (list): List of stock ticker symbols to track
        data_folder (str): Path to data storage directory
        
    Example:
        >>> tracker = StockTracker(['AAPL', 'GOOGL', 'MSFT'])
        >>> tracker.update_data()
        >>> tracker.generate_report()
    """
```

---

## 💡 **Pro Tips:**

1. **Explain WHY, not WHAT**: Code shows what you're doing, comments explain why
2. **Keep comments updated**: Outdated comments are worse than no comments
3. **Use TODO comments**: `# TODO: Add error handling for API failures`
4. **Comment complex algorithms**: Especially financial calculations
5. **Document assumptions**: `# Assumes market is open during update`

**Good comments make your portfolio code professional and maintainable!** 🚀📊