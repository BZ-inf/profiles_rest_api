
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manger for user profile"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # user.set_password(password)
        if password:
            user.set_password(password) #enkrypt password as hash
        user.save(using=self._db) ## saving obj in django

        return user

    def create_superuser(self, email, name, password):
        """Create and ssave a nre superu with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser= True #dziedziczony z PermissionsMixin
        user.is_staff= True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrive full name of user"""
        return self.name

    def get_short_name(self):
        """Retrive short name of user"""
        return self.name
    def __str__(self):
        """Return sting rep of our user"""
        return self.email
