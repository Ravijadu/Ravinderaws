# Generated by Django 4.1.1 on 2022-10-21 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_remove_listing_district_listing_bathrooms_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='photo_1',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_2',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_3',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_4',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_5',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_6',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_main',
        ),
    ]
