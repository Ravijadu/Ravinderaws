# Generated by Django 4.1.1 on 2022-10-13 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='city',
        ),
        migrations.AddField(
            model_name='listing',
            name='district',
            field=models.CharField(default=5, max_length=200),
            preserve_default=False,
        ),
    ]
