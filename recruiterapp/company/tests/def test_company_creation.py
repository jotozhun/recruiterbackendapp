
from django.test import TestCase
from company.models import Company


class TestCompanyCreation(TestCase):
    """Tests creation of a company"""

    def setUp(self):
        self.company_attr = {
            "identifier": "0702557431",
            "name": "Super IT Company",
            "email": "superitcorp001@hotmail.com",
            "description": "Hello my friend, this is my big tech company lol",
            "country": "Ecuador",
            "city": "Guayaquil",
            "zip_code": "1234",
        }

    def test_create_company_success(self):
        """Test that you can create successfully a company"""
        company = Company.objects.create(**self.company_attr)
        self.assertEqual(company.email, self.company_attr['email'])
        self.assertFalse(company.is_verified)
        self.assertFalse(company.is_active)
