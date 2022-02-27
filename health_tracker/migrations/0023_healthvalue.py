# Generated by Django 3.2.4 on 2022-02-27 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health_tracker', '0022_auto_20220226_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_condition', models.CharField(default=None, max_length=100, verbose_name='Health Condition')),
                ('maximum_value', models.IntegerField(blank=True, default=None, null=True, verbose_name='Maximum Value')),
                ('minimum_value', models.IntegerField(blank=True, default=None, null=True, verbose_name='Minimum Value')),
                ('patient_value', models.IntegerField(blank=True, default=None, null=True, verbose_name="Patient's Value")),
                ('health_status', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='health_status', to='health_tracker.healthstatus', verbose_name='Health Status')),
            ],
        ),
    ]
