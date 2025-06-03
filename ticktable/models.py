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
    
    def __str__(self):
        return f"BTC Price: {self.live_price} at {self.timestamp}"
    
    class Meta:
        verbose_name = 'Tick'
        verbose_name_plural = 'Ticks'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['timestamp']),
        ]


# script model currency id,name foregin key as in ticktable