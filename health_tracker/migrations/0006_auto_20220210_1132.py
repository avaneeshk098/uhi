# Generated by Django 3.2.4 on 2022-02-10 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_tracker', '0005_auto_20220209_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default=None, max_length=200, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='medworkerrep',
            name='hcwvid',
            field=models.CharField(default=None, max_length=11, unique=True, verbose_name='Health Care Worker/Vendor ID'),
        ),
    ]
