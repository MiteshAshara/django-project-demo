from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'gender', 'dob', 'city', 'created_at')
    list_filter = ('city',)  # Ensure this is a tuple
    ordering = ('-created_at',)  # Ensure this is a tuple
