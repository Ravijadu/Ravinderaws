# Generated by Django 4.1.1 on 2022-10-21 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_remove_listing_house'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='district',
        ),
        migrations.AddField(
            model_name='listing',
            name='bathrooms',
            field=models.DecimalField(decimal_places=1, default=2, max_digits=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='city',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='garage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(decimal_places=1, default=3, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_5',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='photo_6',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
