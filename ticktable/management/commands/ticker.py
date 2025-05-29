from django.core.management.base import BaseCommand
from ._btc_price_monitor import run_ticker


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Successfully')
        )
        run_ticker()
    