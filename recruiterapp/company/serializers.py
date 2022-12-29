from company import models
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    """Serializer of the Company model"""
    class Meta:
        model = models.Company
        fields = ('id', 'identifier', 'name',
                  'email', 'country',
                  'city', 'zip_code', "created_on")
        read_only_fields = ['id']


class RegisterCompanySerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = models.Company
        fields = ('id', 'identifier', 'name',
                  'email', 'description', 'country',
                  'city', 'zip_code')

    def create(self, validated_data):
        company = models.Company.objects.create(
            **validated_data
        )
        return company


class CompanyEmployerSerializer(serializers.ModelSerializer):
    """Serializer to represent a company employer attributes"""

    class Meta:
        model = models.CompanyEmployer
        fields = ('id', 'company_id', 'user_id', 'role')


class AssignUserToCompanySerializer(serializers.ModelSerializer):
    """Serializer to assign an Employer to a company"""
    class Meta:
        model = models.CompanyEmployer
        fields = ('id', 'company_id', 'user_id', 'role')

    def create(self, validated_data):
        company_employer = models.CompanyEmployer.objects.create(
                            **validated_data)
        return company_employer
