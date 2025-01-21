# Generated by Django 5.1.2 on 2025-01-16 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball_app', '0005_alter_battingstats_year_alter_pitchingstats_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battingstats',
            name='avg',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='battingstats',
            name='on_base_percentage',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='battingstats',
            name='slugging_percentage',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pitchingstats',
            name='era',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pitchingstats',
            name='innings_pitched',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pitchingstats',
            name='k_bb_ratio',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pitchingstats',
            name='strikeouts_per_9',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pitchingstats',
            name='whip',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pitchingstats',
            name='win_percentage',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterUniqueTogether(
            name='battingstats',
            unique_together={('player', 'year')},
        ),
        migrations.AlterUniqueTogether(
            name='pitchingstats',
            unique_together={('player', 'year')},
        ),
    ]
