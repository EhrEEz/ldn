# Generated by Django 4.0.2 on 2023-05-15 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0010_booking_booking_end_date_booking_booking_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_end_date',
            field=models.DateField(verbose_name='Booking End Date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_start_date',
            field=models.DateField(verbose_name='Booking Start Date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_total_days',
            field=models.IntegerField(null=True, verbose_name='Booking Duration'),
        ),
    ]