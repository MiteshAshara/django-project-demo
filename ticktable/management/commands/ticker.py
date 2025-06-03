from django.core.management.base import BaseCommand
from ._btc_price_monitor import run_ticker
from ticktable.models import Script 
import argparse

# def validate_script_id(value):
#     try:
#         id_value = int(value)
#         if id_value <= 0:
#             raise argparse.ArgumentTypeError(f"Script ID must be a positive integer, i have got : '{value}'")
#         return id_value
#     except ValueError:
#         raise argparse.ArgumentTypeError(f"Script ID must be a numeric value, i have got : '{value}'")


class Command(BaseCommand):
    help = "Monitors and displays {script.name} price from Binance WebSocket API"

    def add_arguments(self, parser):
        parser.add_argument(
            '--message', 
            type=str,
            default="Starting BTC price monitor...",
            help='Custom message to display when starting the ticker'
        )
        parser.add_argument(
            '--script_id', 
            # type=validate_script_id, 
            # default=5,
            nargs='+', 
            type=int,
            dest='list',
            required=True, #required for the script to run
            help='ID of the script to monitor (must be a positive integer)'
        )

    def handle(self, *args, **options):
        # print(options['script_id'])
        # script_id = options['script_id'][0]
        script_ids = options['list']
        for script_id in script_ids:
            try:
                script = Script.objects.get(id=script_id)
                print(script.name)
                # print(script.token)
                run_ticker(script)
                self.stdout.write(self.style.SUCCESS(f'Loaded script: {script}'))
            except Script.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Script with {script_id} not found'))
                return 
        
        message = options['message']
        self.stdout.write(
            self.style.SUCCESS(f'Hey, {message}') 
        )
        #run_ticker('enausdt')
        # run_ticker(script)