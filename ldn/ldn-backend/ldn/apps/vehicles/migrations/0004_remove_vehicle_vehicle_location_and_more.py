# Generated by Django 4.0.2 on 2023-05-08 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_remove_vehicledetails_location_area_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_location',
        ),
        migrations.AddField(
            model_name='vehicledetails',
            name='vehicle_location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vehicles.location', verbose_name='Vehicle Location'),
            preserve_default=False,
        ),
    ]
