# Generated by Django 4.1.1 on 2022-10-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OwnerPanel', '0005_rename_photo_main_listing_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo',
            field=models.ImageField(default='', upload_to='photos/%Y/%m/%d/'),
        ),
    ]