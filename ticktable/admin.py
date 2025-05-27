from django.contrib import admin
from .models import TickTable

@admin.register(TickTable)
class TickTableAdmin(admin.ModelAdmin):
    list_display = ('live_price', 'timestamp')
    search_fields = ('live_price',)
    list_filter = ('timestamp',)
