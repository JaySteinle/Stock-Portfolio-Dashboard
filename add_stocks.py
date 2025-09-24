"""
Quick Stock Addition Script
Add new stocks to your tracker without editing config files
"""

from stock_tracker import StockTracker
from config import Config
import sys

def add_stocks(new_symbols):
    """Add new stocks to the tracker (merges with existing symbols)"""
    print(f"🔄 Adding stocks: {', '.join(new_symbols)}")
    
    # Get existing symbols from config
    existing_symbols = Config.DEFAULT_SYMBOLS.copy()
    print(f"📋 Current symbols: {', '.join(existing_symbols)}")
    
    # Add new symbols (avoid duplicates)
    combined_symbols = existing_symbols.copy()
    added_count = 0
    
    for symbol in new_symbols:
        if symbol not in combined_symbols:
            combined_symbols.append(symbol)
            added_count += 1
            print(f"➕ Adding: {symbol}")
        else:
            print(f"⚠️  Already tracking: {symbol}")
    
    if added_count == 0:
        print("ℹ️  No new symbols to add - all are already being tracked!")
        return True
    
    # Create tracker with combined symbols (existing + new)
    tracker = StockTracker(combined_symbols)
    
    # Run update for all symbols
    success = tracker.run_update()
    
    if success:
        print(f"\n✅ Successfully updated tracker with {len(combined_symbols)} total symbols")
        print(f"📊 Added {added_count} new stocks: {', '.join([s for s in new_symbols if s not in existing_symbols])}")
        print("🌐 Check your dashboard for the updated data!")
        print(f"📈 Total portfolio: {', '.join(combined_symbols)}")
    else:
        print(f"\n❌ Failed to update tracker")
    
    return success

def main():
    """Main function for adding stocks"""
    print("📈 Quick Stock Addition Tool")
    print("=" * 40)
    
    if len(sys.argv) > 1:
        # Command line arguments provided
        symbols = [s.upper().strip() for s in sys.argv[1:]]
        add_stocks(symbols)
    else:
        # Interactive mode
        print("\nEnter stock symbols separated by commas (e.g., AAPL,GOOGL,TSLA):")
        user_input = input("Symbols: ").strip()
        
        if user_input:
            symbols = [s.upper().strip() for s in user_input.split(',')]
            add_stocks(symbols)
        else:
            print("❌ No symbols provided.")

if __name__ == "__main__":
    main()