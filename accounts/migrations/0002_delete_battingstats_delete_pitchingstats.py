# Generated by Django 5.1.2 on 2025-01-31 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BattingStats',
        ),
        migrations.DeleteModel(
            name='PitchingStats',
        ),
    ]
