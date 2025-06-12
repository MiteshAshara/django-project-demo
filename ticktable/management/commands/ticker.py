from django.core.management.base import BaseCommand
from ._btc_price_monitor import run_ticker
from ticktable.models import Script 

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
            # dest='list',
            required=True, 
            help='ID of the script to monitor (must be a positive integer)'
        )
    def store_data(data, script):
         if not data or 'c' not in data:
            return
            
    # def handle(self, *args, **options):
    #     # print(options['script_id'])
    #     script_ids = options['list']
    #     for script_id in script_ids:
    #         try:
    #             script = Script.objects.get(id=script_id)
    #             print(script.name)
    #             # print(script.token)
    #             run_ticker(script)
    #             self.stdout.write(self.style.SUCCESS(f'Loaded script: {script}'))
    #         except Script.DoesNotExist:
    #             self.stdout.write(self.style.ERROR(f'Script with {script_id} not found'))
    #             return
        
        # message = options['message']
        # self.stdout.write(
        #     self.style.SUCCESS(f'Hey, {message}') 
        # )
        #run_ticker('enausdt')
        # run_ticker(script)
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Hey"))
        script_ids = options['script_id']
        scripts = list(Script.objects.filter(pk__in=script_ids))

        if not scripts:
            self.stdout.write(self.style.ERROR("No scripts found for the provided IDs."))
            return

        for script in scripts:
            self.stdout.write(self.style.SUCCESS(f"{script.name}"))
        # script=Script.objects.get(pk=5)
        run_ticker(scripts)
