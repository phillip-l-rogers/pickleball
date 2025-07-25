# Generated by Django 5.2.3 on 2025-07-23 21:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tournaments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tournament",
            name="end_date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tournament",
            name="game_day",
            field=models.CharField(
                choices=[
                    ("Monday", "Monday"),
                    ("Tuesday", "Tuesday"),
                    ("Wednesday", "Wednesday"),
                    ("Thursday", "Thursday"),
                    ("Friday", "Friday"),
                    ("Saturday", "Saturday"),
                    ("Sunday", "Sunday"),
                ],
                default="Sunday",
                max_length=10,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tournament",
            name="location",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="tournament",
            name="start_date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
