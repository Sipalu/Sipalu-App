<<<<<<< HEAD
# Generated by Django 4.1.3 on 2022-12-25 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_remove_service_digital'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
=======
# Generated by Django 4.1.3 on 2022-12-25 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_remove_service_digital'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
>>>>>>> 550c397da82c84627a5a585ea40baaaeb7077ad9