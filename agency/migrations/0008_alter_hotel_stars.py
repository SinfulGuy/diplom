# Generated by Django 3.2.12 on 2022-08-24 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0007_alter_hotel_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='stars',
            field=models.IntegerField(max_length=50),
        ),
    ]
