from django.core.management.base import BaseCommand
from ._btc_price_monitor import run_ticker


class Command(BaseCommand):
    help = "Monitors and displays BTC/USDT price from Binance WebSocket API"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Starting BTC price monitor...')
        )
        run_ticker()
