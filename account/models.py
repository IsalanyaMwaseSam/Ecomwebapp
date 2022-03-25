import email
from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

class MyAccountManager(BaseUserManager):
    def _create_user(self, email, username, password, first_name, other_names, phonenumber, Address_1, Address_2):
        if not email:
            raise ValueError("User must have an email")
        if not username:
            raise ValueError("User must have a username")

        user = self.model(
               email = self.normalize_email(email),
               username = username, password=password, first_name = first_name, other_names = other_names,
               phonenumber = phonenumber, Address_1 = Address_1, Address_2 = Address_2
            )   

        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_user(self, email, username, password, first_name=None, other_names=None, phonenumber=None, Address_1=None, Address_2=None):
        return self._create_user(email, username, password,first_name, other_names, phonenumber, Address_1, Address_2)

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, name and password.
        """
        user = self.create_user(email=email,
            username=username,
            password=password,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name='first_name', max_length=60, null=True)
    other_names = models.CharField(verbose_name='other_names', max_length=200, null=True)
    phonenumber = PhoneNumberField(verbose_name='phonenumber', null=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=60, unique=True)
    Address_1 = models.CharField(max_length=60, blank=False, null=True)
    Address_2 = models.CharField(max_length=60, blank=False, null=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyAccountManager()


    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True