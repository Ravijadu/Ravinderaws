# Generated by Django 4.1.1 on 2022-10-16 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OwnerPanel', '0003_listing_photo_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]