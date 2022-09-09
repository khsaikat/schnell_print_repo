# Generated by Django 4.1.1 on 2022-09-08 23:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Printer",
            fields=[
                (
                    "printer_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("printer_name", models.CharField(max_length=200)),
                (
                    "printer_model",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "printer_type",
                    models.CharField(
                        choices=[
                            ("inkjet_cartridge_b&w", "Inkjet-Cartridge-B&W"),
                            ("laser_cartridge_b&w", "Laser-Cartridge-B&W"),
                            ("inkjet_ink_tank_b&w", "Inkjet-Ink-Tank-B&W"),
                            ("laser_ink_tank_b&w", "Laser-Ink-Tank-B&W"),
                            ("inkjet_cartridge_color", "Inkjet-Cartridge-Color"),
                            ("laser_cartridge_color", "Laser-Cartridge-Color"),
                            ("inkjet_ink_tank_color", "Inkjet-Ink-Tank-Color"),
                            ("laser_ink_tank_color", "Laser-Ink-Tank-Color"),
                        ],
                        max_length=200,
                    ),
                ),
                (
                    "printer_company",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "printer_owner",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("printer_description", models.TextField(blank=True, null=True)),
                (
                    "printer_featured_image",
                    models.ImageField(
                        blank=True, default="default.jpg", null=True, upload_to=""
                    ),
                ),
            ],
        ),
    ]
