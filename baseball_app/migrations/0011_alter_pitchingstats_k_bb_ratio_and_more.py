# Generated by Django 5.1.2 on 2025-01-16 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball_app', '0010_alter_pitchingstats_era'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitchingstats',
            name='k_bb_ratio',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='pitchingstats',
            name='strikeouts_per_9',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pitchingstats',
            name='whip',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
