from django.urls import path
from company import views

urlpatterns = [
    path('company/', views.CompanyAPI.as_view(),
         name='company'),
    path('company-employer/', views.CompanyEmployerListView.as_view(),
         name='list-company-employer'),
    path('company-employer/assign', views.AssignUserToCompanyView.as_view(),
         name="assign-company-employer"),
    path('register/', views.RegisterCompanyAPI.as_view(),
         name='company-register'),
]
