# Generated by Django 4.1.1 on 2022-10-23 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('listings', '0019_remove_listing_realtor'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor'),
            preserve_default=False,
        ),
    ]
