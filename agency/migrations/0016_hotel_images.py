# Generated by Django 3.2.12 on 2022-08-31 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0015_alter_hotelimage_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='images',
            field=models.ImageField(null=True, upload_to='hotels/'),
        ),
    ]
