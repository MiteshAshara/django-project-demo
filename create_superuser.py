import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

from django.contrib.auth.models import User

username = 'admin'
email = 'admin@gmail.com'
password = 'admin'

if not User.objects.filter(username=username).exists():
    print(f'Creating superuser {username}')
    User.objects.create_superuser(username=username, email=email, password=password)
    print('Superuser created successfully')
else:
    print(f'Superuser {username} already exists')
