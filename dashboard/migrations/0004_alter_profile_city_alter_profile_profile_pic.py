<<<<<<< HEAD
# Generated by Django 4.1.3 on 2022-12-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Pepsicola', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='static/images/user.jpg', upload_to='static/profile/images'),
        ),
    ]
=======
# Generated by Django 4.1.3 on 2022-12-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Pepsicola', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='static/images/user.jpg', upload_to='static/profile/images'),
        ),
    ]
>>>>>>> 550c397da82c84627a5a585ea40baaaeb7077ad9
