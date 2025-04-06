from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name