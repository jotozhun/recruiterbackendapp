from django.test import TestCase
from django.contrib.auth import get_user_model

from datetime import datetime

class TestUserCreation(TestCase):
    """Tests user creation scenarios."""

    def setUp(self):
        self.test_email="test@example.com"
        self.expected_username="test"
        self.test_password="testpass123"
        self.expected_emails=[
            ("test1@EXAMPLE.com","test1@example.com"),
            ("Test2@Example.com", "Test2@example.com"),
            ("TEST3@EXAMPLE.COM", "TEST3@example.com"),
            ("test4@eXAMPLE.com", "test4@example.com"),
        ]
        self.dateformat="%Y-%m-%d %H:%M"

    def test_user_creation_with_email(self):
        """Test user can be created using email."""
        user = get_user_model().objects.create_user(
            email=self.test_email,
            password=self.test_password,
        )
        self.assertEqual(user.email, self.test_email)
        self.assertTrue(user.check_password(self.test_password))

    def test_normalize_user_email(self):
        """Test the user email normalization"""
        for email, expected in self.expected_emails:
            user = get_user_model().objects.create_user(
                email=email,
                password=self.test_password,
            )
            self.assertEqual(user.email, expected)

    def test_create_user_without_email(self):
        """Test create user without email to raise a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="",
                password=self.test_password,
            )

    def test_create_user_without_password(self):
        """Test create user without password to raise a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=self.test_email,
                password="",
            )

    def test_created_account_date_when_create_user(self):
        """Test the user account datetime to be set after being created with minutes accuracy."""
        user = get_user_model().objects.create_user(
            email=self.test_email,
            password=self.test_password,
        )
        today_datetime = datetime.now()
        today_datetime_to_compare = today_datetime.strftime(self.dateformat)
        user_created_at_datetime = user.created_at.strftime(self.dateformat)
        self.assertEqual(today_datetime_to_compare, user_created_at_datetime)

    def test_create_superuser(self):
        """Test create a superuser."""
        user = get_user_model().objects.create_superuser(
            email=self.test_email,
            password=self.test_password,
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
    