# Generated by Django 3.2.12 on 2022-08-16 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0004_auto_20220816_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelbooking',
            name='booking_type',
        ),
    ]
