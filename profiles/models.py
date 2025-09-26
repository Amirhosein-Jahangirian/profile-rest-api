from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """the manager to create users and superusers in user model"""

    def create_user(self, email, first_name, last_name, password=None):
        """create new user profile"""

        if not email:
            raise ValueError('user must have an email address')

        if not first_name:
            raise ValueError('user must have a first name')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password):
        superuser = self.create_user(email, first_name, password)
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.save(using=self._db)

        return superuser


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database models for users in system"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', ]

    def get_full_name(self):
        """retrieve full name of the user"""
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        """retrieve full name of the user"""
        return self.first_name

    def __str__(self):
        """retuen string representation of our user"""
        return self.email
