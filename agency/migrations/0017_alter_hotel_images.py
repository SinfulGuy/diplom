# Generated by Django 3.2.12 on 2022-08-31 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0016_hotel_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='images',
            field=models.ImageField(upload_to='hotels/'),
        ),
    ]
