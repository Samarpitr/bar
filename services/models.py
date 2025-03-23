from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=None, blank=True, null=True)
    logo = models.ImageField(upload_to='services/')
    price = models.IntegerField(default=0, blank=True, null=True)
    barcode = models.ImageField(upload_to='barcodes/', blank=True, null=True)
    def __str__(self):
        return self.name