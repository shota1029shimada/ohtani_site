# Generated by Django 5.1.2 on 2025-01-16 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball_app', '0006_alter_battingstats_avg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitchingstats',
            name='k_bb_ratio',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
    ]
