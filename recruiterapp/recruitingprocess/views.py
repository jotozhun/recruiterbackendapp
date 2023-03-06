from recruitingprocess import models
from recruitingprocess import serializers as recruitingprocess_serializers
from rest_framework.response import Response
from rest_framework import generics, permissions, status


class JobRoleAPI(generics.GenericAPIView):
    """
    JobRole View
    """
    serializer_class = recruitingprocess_serializers.JobRoleSerializer

    def post(self, request, *args, **kwargs):
        """Create a Job Role"""
        

class RecruitingProcessAPI(generics.GenericAPIView):
    """
    RecruitingProcess View
    """
    serializer_class = recruitingprocess_serializers.RecruitingProcessSerializer
    
    def post(self, request, *args, **kwargs):
        """Create a Recruiting Process"""
        

class CandidateAPI(generics.GenericAPIView):
    """
    CandidateProcess View
    """
    serializer_class = recruitingprocess_serializers.CandidateSerializer
    
    def post(self, request, *args, **kwargs):
        """Create a Candidate"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        