from celery import shared_task
import time
from datetime import datetime

# @shared_task
# def add(x, y):
#     return x + y

# @shared_task(name="multiply_task")
# def multiply(x, y):
#     return x * y

# @shared_task
# def very_long_task(minutes=2): #2 minutes
#     """Task that runs for several minutes to be visible in RabbitMQ"""
#     seconds = minutes * 60
#     time.sleep(seconds)
#     return f"Very long task completed after {minutes} minutes"

# task save to db store ticks after celery store all ticks in db
@shared_task
def save_ticks_to_db(tick):
    """
    Save a list of ticks to the database.
    This is a placeholder function and should be implemented
    with actual database logic.
    """
    try:
        from ticktable.models import Tick
        
        tick_data = {
            'live_price': tick.get('live_price'),
            'timestamp': tick.get('timestamp'),
            'total_trades': tick.get('tradevolume'),
            'script_id': tick.get('script_id')
        }
        
        ticks = Tick(**tick_data)
        # Save to database
        ticks.save()
        
        return f"Successfully saved tick data at {ticks.timestamp}"
    
    except Exception as e:
        return f"Error saving tick data: {str(e)}"
        # live price,timestamp,tradevolume,script_id dirctory
