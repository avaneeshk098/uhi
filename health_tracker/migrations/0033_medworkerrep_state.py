# Generated by Django 3.2.4 on 2022-03-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_tracker', '0032_auto_20220314_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='medworkerrep',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='State/Union Territory'),
        ),
    ]
