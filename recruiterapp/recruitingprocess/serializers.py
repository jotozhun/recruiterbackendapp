from recruitingprocess import models
from rest_framework import serializers


class JobRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobRoleModel
        fields = ['company_id', 'title']


# Candidate Serializer
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CandidateModel
        fields = ['id', 'company_id', 'name', 'lastname', 'contact_email']
        

class RecruitingProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RecruitingProcessModel
        fields = ['id', 'company_id', 'candidate', 'role', 'status', 'started_on']
        