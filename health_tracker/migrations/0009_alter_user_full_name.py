# Generated by Django 3.2.4 on 2022-02-10 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_tracker', '0008_alter_user_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Full Name'),
        ),
    ]
