from django.db import models
from django.utils import timezone

class Script(models.Model):
    """
    Model for storing script information with a foreign key to Tick
    """
    name = models.CharField(max_length=100, unique=True)
    token = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Script'
        verbose_name_plural = 'Scripts'
        indexes = [
            models.Index(fields=['name']),
        ]


class Tick(models.Model):
    """
    Model for storing all BTC/USDT tick data with precise price information
    """
    script = models.ForeignKey(Script, on_delete=models.RESTRICT)
    live_price = models.DecimalField(max_digits=24, decimal_places=10)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    event_type = models.CharField(max_length=50, null=True, blank=True)  # "e": "24hrTicker"
    event_time = models.BigIntegerField(null=True, blank=True)  # "E": timestamp
    symbol = models.CharField(max_length=20, null=True, blank=True)  # "s": "BTCUSDT"
    price_change = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)  # "p"
    price_change_percent = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)  # "P"
    weighted_avg_price = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)  # "w"
    first_trade_price = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)  # "x"
    last_price = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)  # "c"
    last_quantity = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)  # "Q"
    best_bid_price = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)  # "b"
    best_bid_quantity = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)  # "B"
    best_ask_price = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)  # "a"
    best_ask_quantity = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)  # "A"
    open_price = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)  # "o"
    high_price = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)  # "h"
    low_price = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)  # "l"
    total_traded_base_volume = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)  # "v"
    total_traded_quote_volume = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)  # "q"
    statistics_open_time = models.BigIntegerField(null=True, blank=True)  # "O"
    statistics_close_time = models.BigIntegerField(null=True, blank=True)  # "C"
    first_trade_id = models.BigIntegerField(null=True, blank=True)  # "F"
    last_trade_id = models.BigIntegerField(null=True, blank=True)  # "L"
    total_trades = models.BigIntegerField(null=True, blank=True)  # "n"
    
    def __str__(self):
        return f"BTC Price: {self.live_price} at {self.timestamp}"
    
    class Meta:
        verbose_name = 'Tick'
        verbose_name_plural = 'Ticks'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['timestamp']),
        ]