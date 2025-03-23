from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default=None, blank=True, null=True)
    file = models.FileField(upload_to='notice/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title