# Consolidated migration file for the `customers` app.

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # No dependencies for the initial migration.
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, default='')),
                ('last_name', models.CharField(max_length=100, default='')),
                ('email', models.EmailField(max_length=254, unique=True, default='')),
                ('address', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=15, default='')),
                ('city', models.CharField(max_length=100, default='')),
                ('pincode', models.CharField(max_length=10, default='')),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(
                    max_length=1,
                    choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
                    default='O'
                )),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
