from django.shortcuts import render
from .models import Customer

def index_view(request):
    return render(request, 'index.html', {'title': 'iLanding'})

def about_view(request):
    return render(request, 'about.html', {'title': 'About | iLanding'})

def features_view(request):
    return render(request, 'features.html', {'title': 'Features | iLanding'})

def contact_view(request):
    return render(request, 'contact-us.html', {'title': 'Contact | iLanding'})

def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'title': 'Customer List',
        'customers': customers
    }
    return render(request, 'customer.html', context)
