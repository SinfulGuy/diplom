# Generated by Django 3.2.12 on 2022-08-25 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0010_alter_hotel_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='location',
            field=models.CharField(choices=[('Minsk', 'Minsk'), ('Brest', 'Brest'), ('Vitebsk', 'Vitebsk'), ('Mogilev', 'Mogilev'), ('Gomel', 'Gomel'), ('Grodno', 'Grodno')], max_length=10),
        ),
    ]