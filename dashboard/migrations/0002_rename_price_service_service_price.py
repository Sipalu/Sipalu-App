# Generated by Django 4.1.3 on 2022-12-21 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='price',
            new_name='service_price',
        ),
    ]