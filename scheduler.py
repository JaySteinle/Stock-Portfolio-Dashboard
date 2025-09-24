"""
Automated scheduler for stock data updates
Runs the stock tracker at specified intervals
"""

import schedule
import time
import logging
from datetime import datetime
import os
from stock_tracker import StockTracker

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('stock_tracker.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class StockScheduler:
    def __init__(self, symbols=None):
        """Initialize the scheduler"""
        self.tracker = StockTracker(symbols)
        self.is_running = False
        
    def update_job(self):
        """Job function for scheduled updates"""
        try:
            logger.info("🕐 Scheduled update starting...")
            success = self.tracker.run_update()
            
            if success:
                logger.info("✅ Scheduled update completed successfully")
            else:
                logger.error("❌ Scheduled update failed")
                
        except Exception as e:
            logger.error(f"❌ Error during scheduled update: {str(e)}")
    
    def start_scheduler(self, update_frequency="1h"):
        """Start the scheduler with specified frequency"""
        logger.info("🚀 Starting Stock Tracker Scheduler...")
        logger.info(f"📅 Update frequency: {update_frequency}")
        
        # Clear existing jobs
        schedule.clear()
        
        # Schedule based on frequency
        if update_frequency == "15m":
            schedule.every(15).minutes.do(self.update_job)
        elif update_frequency == "30m":
            schedule.every(30).minutes.do(self.update_job)
        elif update_frequency == "1h":
            schedule.every().hour.do(self.update_job)
        elif update_frequency == "2h":
            schedule.every(2).hours.do(self.update_job)
        elif update_frequency == "daily":
            schedule.every().day.at("09:30").do(self.update_job)  # Market open
        else:
            logger.error(f"❌ Invalid frequency: {update_frequency}")
            return
        
        # Run initial update
        logger.info("🔄 Running initial update...")
        self.update_job()
        
        self.is_running = True
        logger.info(f"✅ Scheduler started successfully")
        
        # Keep the scheduler running
        try:
            while self.is_running:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
                
        except KeyboardInterrupt:
            logger.info("🛑 Scheduler stopped by user")
            self.stop_scheduler()
    
    def stop_scheduler(self):
        """Stop the scheduler"""
        self.is_running = False
        schedule.clear()
        logger.info("🛑 Scheduler stopped")

def main():
    """Main function for command-line usage"""
    print("📊 Stock Tracker Scheduler")
    print("=" * 50)
    
    # Configuration options
    frequencies = {
        "1": ("15m", "Every 15 minutes"),
        "2": ("30m", "Every 30 minutes"), 
        "3": ("1h", "Every hour"),
        "4": ("2h", "Every 2 hours"),
        "5": ("daily", "Daily at 9:30 AM")
    }
    
    print("\nSelect update frequency:")
    for key, (freq, desc) in frequencies.items():
        print(f"{key}. {desc}")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice in frequencies:
        frequency, description = frequencies[choice]
        print(f"\n✅ Selected: {description}")
        
        # Initialize and start scheduler
        scheduler = StockScheduler(['SPY', 'QQQ', 'GLD', 'ARKK', 'TLT'])
        
        print("\n🚀 Starting scheduler... Press Ctrl+C to stop")
        scheduler.start_scheduler(frequency)
        
    else:
        print("❌ Invalid choice. Exiting.")

if __name__ == "__main__":
    main()