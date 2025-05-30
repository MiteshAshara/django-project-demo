from django.core.management.base import BaseCommand
from ._btc_price_monitor import run_ticker


class Command(BaseCommand):
    help = "Monitors and displays BTC/USDT price from Binance WebSocket API"
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--message', #script id
            default="Starting BTC price monitor...",
            help='Custom message to display when starting the ticker'
        )

    def handle(self, *args, **options):
        message = options['message']
        self.stdout.write(
            self.style.SUCCESS(f'Hey, {message}') #pass agrument on docker cmd like python manage.py ticker --message="Test" // Hey , Test
            #  self.style.SUCCESS(f'Hey, Test Argument')
        )
        # run_ticker('enausdt')
        run_ticker('btcusdt')
    
    # def name(name,age): #Postional argument (exact postion known for run ,Order matters)
    #     print(f"Name: {name}, Age: {age}")
    # name("John", 30)  

    # def greet(name, age): # Named arguments (Order doesn't matter)
    #     return f"Hello {name}, you are {age} years old."
    # print(greet(name="Bob", age=25))  

    # def print_args(*args, **kwargs):  # Positional and keyword arguments
    #     print("Positional arguments:", args)
    #     print("Keyword arguments:", kwargs)
    # print_args(1, 2, 3, name="Alice", age=30) 