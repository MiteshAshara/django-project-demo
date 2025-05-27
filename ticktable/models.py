from django.db import models
from django.utils import timezone

class TickTable(models.Model):
    """
    Model for storing all BTC/USDT tick data with precise price information
    """
    live_price = models.DecimalField(max_digits=20, decimal_places=10)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
    
    def __str__(self):
        return f"BTC Price: {self.live_price} at {self.timestamp}"
    
    class Meta:
        verbose_name = 'Tick Table'
        verbose_name_plural = 'Tick Tables'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['timestamp']),
        ]
