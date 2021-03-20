from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


# Create your models here.
from users.managers import CustomUserManager


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_users'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
