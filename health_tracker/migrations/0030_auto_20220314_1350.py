# Generated by Django 3.2.4 on 2022-03-14 08:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_tracker', '0029_alter_healthvalue_condition_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='medworkerrep',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='medworkerrep',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='City/Town'),
        ),
        migrations.AddField(
            model_name='medworkerrep',
            name='pincode',
            field=models.CharField(blank=True, default=None, max_length=6, null=True, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AddField(
            model_name='medworkerrep',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='healthvalue',
            name='maximum_value',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Maximum Value'),
        ),
        migrations.AlterField(
            model_name='healthvalue',
            name='minimum_value',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Minimum Value'),
        ),
        migrations.AlterField(
            model_name='healthvalue',
            name='patient_value',
            field=models.FloatField(default=None, verbose_name="Patient's Value"),
        ),
    ]
