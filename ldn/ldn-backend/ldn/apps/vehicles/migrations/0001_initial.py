# Generated by Django 4.0.2 on 2023-05-08 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Vehicle Name')),
                ('reg_no', models.CharField(max_length=20, verbose_name='Vehicle Registration Number')),
                ('on_trip', models.BooleanField(default=False, verbose_name='Vehicle is on trip')),
                ('seats', models.IntegerField(verbose_name='Vehicle Seat Limit')),
                ('color_name', models.CharField(max_length=50, verbose_name='Vehicle Color Name')),
                ('color_code', models.CharField(max_length=6, verbose_name='Vehicle Color Code')),
                ('model_name', models.CharField(max_length=100, verbose_name='Vehicle Model Name')),
                ('model_manufacturer', models.CharField(max_length=100, verbose_name='Vehicle Model Manufacturer')),
                ('is_active', models.BooleanField(default=True, verbose_name='Vehicle is active')),
                ('slug', models.TextField(blank=True, null=True, unique=True, verbose_name='Vehicle Slug')),
                ('vehicle_image', models.ImageField(upload_to='vehicle_image', verbose_name='Vehicle Image')),
                ('vehicle_daily_price', models.DecimalField(decimal_places=2, help_text='Cost of renting the Vehicle for a day', max_digits=6, verbose_name='Vehicle Price')),
                ('vehicle_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Vehicle Owner')),
            ],
            options={
                'verbose_name_plural': 'Vehicles',
                'ordering': ['-modification_date', '-creation_date', 'name'],
            },
        ),
        migrations.CreateModel(
            name='VehicleDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('registration_document', models.ImageField(upload_to='vehicle_details', verbose_name='Vehicle Bluebook Information')),
                ('vehicle_verified', models.BooleanField(default=False, verbose_name='Vehicle Verification')),
                ('vehicle_main', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle', to='vehicles.vehicle')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
