# Generated by Django 5.1.2 on 2025-01-16 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball_app', '0008_alter_pitchingstats_innings_pitched'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitchingstats',
            name='innings_pitched',
            field=models.FloatField(),
        ),
    ]
