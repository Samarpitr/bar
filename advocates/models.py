from django.db import models

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> None:
        return self.name
    
class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> None:
        return self.name
    

class Advocate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default=None, blank=True, null=True)
    phone = models.CharField(max_length=15, default=None, blank=True, null=True)
    address = models.TextField(default=None, blank=True, null=True)
    city = models.CharField(max_length=50, default=None, blank=True, null=True)
    state = models.CharField(max_length=50, default=None, blank=True, null=True)
    country = models.CharField(max_length=50, default=None, blank=True, null=True)
    zip = models.CharField(max_length=10, default=None, blank=True, null=True)
    firm = models.CharField(max_length=100, default=None, blank=True, null=True)
    practicing_since = models.DateTimeField(auto_now_add=True)
    practice_areas = models.ManyToManyField(Area)
    registration_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    aibe_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    languages = models.ManyToManyField(Language)
    profile_image = models.ImageField(upload_to='advocates/profile_images/', default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    @property
    def roles(self):
        return AdvocateRole.objects.filter(advocate=self)

    def __str__(self) -> None:
        return self.name
        

class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=None, blank=True, null=True)

    def __str__(self) -> None:
        return self.name
    

class AdvocateRole(models.Model):
    advocate = models.ForeignKey(Advocate, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    appointed_on = models.DateTimeField()
    relieved_on = models.DateTimeField(default=None, blank=True, null=True)
    session = models.CharField(max_length=100, default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ordering = ['appointed_on'] 
    
    def __str__(self) -> None:
        return f'{self.advocate.name} - {self.role.name}'