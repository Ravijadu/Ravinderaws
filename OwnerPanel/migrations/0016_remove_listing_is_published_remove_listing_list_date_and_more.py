# Generated by Django 4.1.1 on 2022-10-21 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OwnerPanel', '0015_rename_hostel_name_listing_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='list_date',
        ),
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
            name='photo_main',
        ),
    ]