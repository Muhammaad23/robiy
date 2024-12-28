# Generated by Django 5.1.3 on 2024-12-21 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Park",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="parks/images/"),
                ),
                ("description", models.TextField()),
                ("working_hours", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=300)),
                ("phone", models.CharField(max_length=15)),
                ("location", models.CharField(max_length=200)),
                ("is_open_now", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Attraction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="parks_images/"),
                ),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("age_group", models.CharField(max_length=100)),
                (
                    "park",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attractions",
                        to="parks.park",
                    ),
                ),
            ],
        ),
    ]