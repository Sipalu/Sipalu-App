# Generated by Django 4.1.3 on 2022-12-22 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_remove_order_status_orderitem_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='service',
        ),
    ]