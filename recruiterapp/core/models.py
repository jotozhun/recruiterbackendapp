from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)

class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, password, **extra_fields):
        """Create a user"""
        if not email or not password:
            raise ValueError("Email or password not provided")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and return a new superuser."""
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Base user to create"""
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=128, null=False, default="def_user")
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()
