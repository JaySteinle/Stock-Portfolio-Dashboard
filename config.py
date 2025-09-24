"""
Configuration settings for the Stock Tracker
"""

import os
from typing import List, Dict

class Config:
    """Configuration class for stock tracker settings"""
    
    # Default ETF symbols to track
    DEFAULT_SYMBOLS: List[str] = ['SPY', 'QQQ', 'GLD', 'ARKK', 'TLT']
    
    # Data fetching settings
    DEFAULT_PERIOD: str = "1y"  # 1 year of historical data
    UPDATE_FREQUENCY: str = "1h"  # Default update frequency
    
    # File paths
    DATA_FOLDER: str = os.path.dirname(os.path.abspath(__file__))
    PORTFOLIO_SUMMARY_FILE: str = "Portfolio_Summary.xlsx"
    CONSOLIDATED_DATA_FILE: str = "Consolidated_Historical_Data.xlsx"
    LOG_FILE: str = "stock_tracker.log"
    
    # Risk-free rate for Sharpe ratio calculation (annual)
    RISK_FREE_RATE: float = 0.02  # 2%
    
    # Moving averages periods
    MA_SHORT_PERIOD: int = 20
    MA_LONG_PERIOD: int = 50
    
    # Portfolio allocation weights (equal weight by default)
    PORTFOLIO_WEIGHTS: Dict[str, float] = {
        'SPY': 0.25,   # S&P 500
        'QQQ': 0.25,   # NASDAQ 100
        'GLD': 0.20,   # Gold
        'ARKK': 0.15,  # Innovation ETF
        'TLT': 0.15    # Long-term Treasury
    }
    
    # Streamlit dashboard settings
    DASHBOARD_TITLE: str = "📊 Interactive Stock Tracker Dashboard"
    DASHBOARD_ICON: str = "📈"
    DASHBOARD_LAYOUT: str = "wide"
    
    # API settings (if needed for future enhancements)
    API_TIMEOUT: int = 30  # seconds
    MAX_RETRIES: int = 3
    
    # Visualization settings
    CHART_HEIGHT: int = 400
    CHART_COLORS: List[str] = [
        '#1f77b4',  # Blue
        '#ff7f0e',  # Orange  
        '#2ca02c',  # Green
        '#d62728',  # Red
        '#9467bd'   # Purple
    ]
    
    @classmethod
    def get_symbol_color(cls, symbol: str) -> str:
        """Get color for a specific symbol"""
        symbol_index = cls.DEFAULT_SYMBOLS.index(symbol) if symbol in cls.DEFAULT_SYMBOLS else 0
        return cls.CHART_COLORS[symbol_index % len(cls.CHART_COLORS)]
    
    @classmethod
    def validate_symbols(cls, symbols: List[str]) -> List[str]:
        """Validate and return list of valid symbols"""
        if not symbols:
            return cls.DEFAULT_SYMBOLS
        
        # Filter out invalid symbols (basic validation)
        valid_symbols = [symbol.upper().strip() for symbol in symbols if symbol.strip()]
        return valid_symbols if valid_symbols else cls.DEFAULT_SYMBOLS
    
    @classmethod
    def get_excel_file_path(cls, symbol: str) -> str:
        """Get full path for symbol's Excel file"""
        return os.path.join(cls.DATA_FOLDER, f"{symbol}.xlsx")
    
    @classmethod
    def get_portfolio_weights(cls, symbols: List[str]) -> Dict[str, float]:
        """Get portfolio weights for given symbols"""
        if not symbols:
            return cls.PORTFOLIO_WEIGHTS
        
        # Equal weight if symbol not in predefined weights
        equal_weight = 1.0 / len(symbols)
        weights = {}
        
        for symbol in symbols:
            weights[symbol] = cls.PORTFOLIO_WEIGHTS.get(symbol, equal_weight)
        
        # Normalize weights to sum to 1.0
        total_weight = sum(weights.values())
        if total_weight > 0:
            weights = {k: v / total_weight for k, v in weights.items()}
        
        return weights

# Environment-specific configurations
class DevelopmentConfig(Config):
    """Development environment configuration"""
    DEBUG = True
    UPDATE_FREQUENCY = "15m"  # More frequent updates for development

class ProductionConfig(Config):
    """Production environment configuration"""
    DEBUG = False
    UPDATE_FREQUENCY = "1h"  # Standard hourly updates for production

# Select configuration based on environment
def get_config():
    """Get configuration based on environment variable"""
    env = os.getenv('STOCK_TRACKER_ENV', 'development').lower()
    
    if env == 'production':
        return ProductionConfig()
    else:
        return DevelopmentConfig()

# Global configuration instance
config = get_config()