from django.db import models

# Create your models here.
class RecruitingProcessModel(models.Model):
    """Model of process information"""
    company_id = models.ForeignKey(
        "company.Company",
        on_delete=models.CASCADE,
    )
    candidate = models.ForeignKey(
        "recruitingprocess.CandidateModel",
        on_delete=models.CASCADE,
    )
    role = models.CharField(max_length=64)
    status = models.CharField(max_length=32, default="Started")
    started_on = models.DateTimeField(auto_now=True)
    
    
class JobRoleClass(models.Model):
    """Model that represents a job position in a company"""
    company_id = models.ForeignKey(
        "company.Company",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=256)


class CandidateModel(models.Model):
    """Model of the candidate that is interviewed"""
    company_id = models.ForeignKey(
        "company.Company",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    contact_email = models.EmailField(max_length=64)
    