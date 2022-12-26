from django.db import models

# Create your models here.

class Company(models.Model):
    """Class for Company"""
    identifier = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254, unique=True)
    description = models.TextField(max_length=254, default="Initial description")
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=10)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    verified_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
