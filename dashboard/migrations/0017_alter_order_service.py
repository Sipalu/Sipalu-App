# Generated by Django 4.1.3 on 2022-12-22 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_alter_order_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.service'),
        ),
    ]