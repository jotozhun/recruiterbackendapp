from django.db import models
from django.conf import settings


class Company(models.Model):
    """Model for Company"""
    identifier = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254, unique=True)
    description = models.TextField(max_length=254,
                                   default="Initial description")
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=10)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    verified_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class CompanyEmployer(models.Model):
    """Model that shows the employees of a Company"""
    company_id = models.ForeignKey(
        "company.Company",
        on_delete=models.CASCADE,
    )
    user_id = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    role = models.CharField(max_length=32, default="Recruiter")
    added_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user_id.name} - {self.user_id.email} - " + self.role
