from company.models import Company
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    """Serializer of the Company model"""
    class Meta:
        model = Company
        fields = ['id', 'identifier', 'name',
                  'email', 'country',
                  'city', 'zip_code', "created_on"]

class RegisterCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'identifier', 'name',
                  'email', 'description', 'country',
                  'city', 'zip_code')

    def create(self, validated_data):
        company = Company.objects.create(
            identifier=validated_data['identifier'],
            name=validated_data['name'],
            email=validated_data['email'],
            description=validated_data['description'],
            country=validated_data['country'],
            city=validated_data['city'],
            zip_code=validated_data['zip_code'],
        )
        return company
