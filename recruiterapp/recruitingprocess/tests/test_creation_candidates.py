
from django.test import TestCase

from recruitingprocess.models import CandidateModel
from company.models import Company


class TestCandidateCreation(TestCase):
    """Tests for creation of candidates"""
    
    def setUp(self):
        self.test_company = Company.objects.create({
            "identifier": "0702557431",
            "name": "Super IT Company",
            "email": "superitcorp001@hotmail.com",
            "description": "Hello my friend, this is my big tech company lol",
            "country": "Ecuador",
            "city": "Guayaquil",
            "zip_code": "1234",
        })
        self.candidate_attr = {
            "company_id": self.test_company,
            "name": "Pedro",
            "lastname": "Yikes",
            "contact_email": "pedroyikes24@testmail.com",
        }
    
    def test_create_candidate_success(self):
        candidate = CandidateModel.objects.create(**self.candidates_attr)
        self.assertTrue(candidate.name, self.candidate_attr["name"])
        self.assertTrue(candidate.lastname, self.candidate_attr["lastname"])
        self.assertTrue(candidate.contact_email, self.candidate_attr["contact_email"])
