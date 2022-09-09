from django.db import models
import uuid


class Printer(models.Model):
    PRINTER_TYPE = (
        ('inkjet_cartridge_b&w', 'Inkjet-Cartridge-B&W'),
        ('laser_cartridge_b&w', 'Laser-Cartridge-B&W'),
        ('inkjet_ink_tank_b&w', 'Inkjet-Ink-Tank-B&W'),
        ('laser_ink_tank_b&w', 'Laser-Ink-Tank-B&W'),
        ('inkjet_cartridge_color', 'Inkjet-Cartridge-Color'),
        ('laser_cartridge_color', 'Laser-Cartridge-Color'),
        ('inkjet_ink_tank_color', 'Inkjet-Ink-Tank-Color'),
        ('laser_ink_tank_color', 'Laser-Ink-Tank-Color')
    )

    printer_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    printer_name = models.CharField(max_length=200)
    printer_model = models.CharField(max_length=200, null=True, blank=True)
    printer_type = models.CharField(max_length=200, choices=PRINTER_TYPE)
    printer_company = models.CharField(max_length=200, null=True, blank=True)
    printer_owner = models.CharField(max_length=200, null=True, blank=True)
    printer_description = models.TextField(null=True, blank=True)
    printer_featured_image = models.ImageField(null=True, blank=True, default='default.jpg')

    def __str__(self):
        return self.printer_name
