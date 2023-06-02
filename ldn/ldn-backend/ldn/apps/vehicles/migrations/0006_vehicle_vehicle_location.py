# Generated by Django 4.0.2 on 2023-05-08 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0005_remove_vehicledetails_vehicle_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vehicles.location', verbose_name='Vehicle Location'),
            preserve_default=False,
        ),
    ]