from company import models
from company import serializers as company_serializers
from rest_framework.response import Response
from rest_framework import generics, permissions, status


class CompanyAPI(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated,]
    serializer_class = company_serializers.CompanySerializer

    def get_queryset(self):
        return models.Company.objects.all()


class RegisterCompanyAPI(generics.GenericAPIView):
    """
    Company View
    """
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = company_serializers.RegisterCompanySerializer

    def post(self, request, *args, **kwargs):
        """Creates a company"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # company = serializer.validated_data
        serializer.save()
        company_data = serializer.data
        company = models.Company.objects.get(id=company_data['id'])

        comp_employer = models.CompanyEmployer.objects.create(
            company_id=company,
            user_id=request.user,
        )
        comp_employer.save()

        return Response({
            'company':  self.serializer_class(company_data,
                        context=self.get_serializer_context()).data,
            }, status=status.HTTP_201_CREATED
        )


class CompanyEmployerListView(generics.ListAPIView):
    """
    List all the employers of all the companies
    """
    # permission_classes = [permissions.IsAdminUser,]
    serializer_class = company_serializers.CompanyEmployerSerializer

    def get_queryset(self):
        all_employers = models.CompanyEmployer.objects.all()
        return all_employers


class AssignUserToCompanyView(generics.CreateAPIView):
    """"""
    # permission_classes = [permissions.IsAuthenticated,]
    serializer_class = company_serializers.AssignUserToCompanySerializer

    def post(self, request, *args, **kwargs):
        """Assigns a user to a created company"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
