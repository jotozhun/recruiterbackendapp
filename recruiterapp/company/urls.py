from django.urls import path
from company.views import RegisterCompanyAPI

urlpatterns = [
    path('register/', RegisterCompanyAPI.as_view(), name='company-register'),
]