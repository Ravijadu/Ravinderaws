# Generated by Django 4.1.1 on 2022-10-24 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='description',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='email',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='phone',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(default=None, upload_to='photos/%Y/%m/%d/'),
        ),
    ]