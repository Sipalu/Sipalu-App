# Generated by Django 4.1.3 on 2022-12-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_alter_order_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=True, null=True),
        ),
    ]