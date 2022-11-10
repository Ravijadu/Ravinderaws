# Generated by Django 4.1.1 on 2022-10-24 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0003_alter_realtor_description_alter_realtor_email_and_more'),
        ('listings', '0023_listing_realtor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='realtors.realtor'),
        ),
    ]