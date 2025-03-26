from django.db import models

class Officers(models.Model):
    name = models.CharField(max_length=100)
    position= models.CharField(max_length=100)
    rank = models.IntegerField()
    phone = models.CharField(max_length=100, default=None, blank=True, null=True)
    image = models.ImageField(upload_to='officer/images')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name