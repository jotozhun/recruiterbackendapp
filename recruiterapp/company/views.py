
from company.models import Company
from company.serializers import RegisterCompanySerializer, CompanySerializer
from rest_framework.response import Response
from rest_framework import generics, permissions, status

class RegisterCompanyAPI(generics.GenericAPIView):
    """
    Company View
    """
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = RegisterCompanySerializer

    def post(self, request, *args, **kwargs):
        """Creates a company"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # company = serializer.validated_data
        serializer.save()
        company_data = serializer.data

        return Response({
            'company':  CompanySerializer(company_data, context=self.get_serializer_context()).data,
            }, status=status.HTTP_201_CREATED 
        )
