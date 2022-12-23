from django.test import TestCase
from core.encryption import TokenEncrypter
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from datetime import datetime, timedelta

class TestTokenEncryption(TestCase):
    """Tests the token encryption scenarios"""

    def setUp(self):
        self.test_user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpass123',
        )
        self.token_encrypter = TokenEncrypter()
        self.date_format = "%Y-%m-%d %H"

    def test_user_token_encryption(self):
        """Checks encryption an decryption of user token"""
        token = Token.objects.create(user=self.test_user).key
        token_encrypted = self.token_encrypter.encrypt_user_token(token)
        token_decrypted = self.token_encrypter.decrypt_user_token(token_encrypted)
        self.assertTrue('token' in token_decrypted)
        self.assertEqual(token, token_decrypted['token'])

    def test_user_token_expiration(self):
        """Check the user token expiration"""
        token = Token.objects.create(user=self.test_user).key
        # Mocking wait of more than the expire date
        token_encrypted = self.token_encrypter.encrypt_user_token(token, 0)
        token_decrypted = self.token_encrypter.decrypt_user_token(token_encrypted)
        self.assertTrue('error' in token_decrypted)
