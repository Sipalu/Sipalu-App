# Generated by Django 4.1.3 on 2022-12-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_price_service_service_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
