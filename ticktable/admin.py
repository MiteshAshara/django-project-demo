from django.contrib import admin
from .models import Tick,Script

@admin.register(Tick)
class TickTableAdmin(admin.ModelAdmin):
    list_display = ('live_price', 'event_type', 'event_time', 'symbol', 'price_change', 'price_change_percent',
                    'weighted_avg_price', 'first_trade_price', 'last_price', 'last_quantity', 'best_bid_price',)
    search_fields = ('live_price',)
    list_filter = ('timestamp','script_id',)

admin.site.register(Script)