# Generated by Django 4.1.1 on 2022-10-16 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OwnerPanel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='photo_main',
        ),
    ]
