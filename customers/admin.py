from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'gender', 'dob', 'city', 'created_at')
    list_filter = ('city',) 
    ordering = ('-created_at',)
