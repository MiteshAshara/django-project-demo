from django.db import models
from django.core.validators import RegexValidator

class Custpmer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    city = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10, validators=[
        RegexValidator(regex=r'^\d{10}$', message='Mobile number must be 10 digits')
    ])
    email = models.EmailField(unique=True)
    address = models.TextField()
    pincode = models.CharField(max_length=6, validators=[
        RegexValidator(regex=r'^\d{6}$', message='Pincode must be 6 digits')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
