from django.db import models
from django.utils import timezone

class Customer(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    dob = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    phone_number = models.CharField(max_length=15, default='')
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, default='')
    pincode = models.CharField(max_length=10, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"