from django.contrib import admin
from .models import Tick,Script

@admin.register(Tick)
class TickTableAdmin(admin.ModelAdmin):
    list_display = ('live_price', 'timestamp')
    search_fields = ('live_price',)
    list_filter = ('timestamp',)

admin.site.register(Script)