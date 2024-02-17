import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Create and return a regular user with an email and password
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Create and return a superuser with an email and password
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    uid = models.IntegerField(null=False, editable=False)
    # Add your custom fields here
    email = models.EmailField(unique=True, null=False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=11, null=False)
    birth_date = jmodels.jDateField(null=True, blank=True)

    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.OTHER)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # save jalali datetime
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(default=timezone.now)
    # save jalali datetime
    j_created = jmodels.jDateTimeField(auto_now_add=True)
    j_updated = jmodels.jDateTimeField(auto_now=True)

    last_IP = models.GenericIPAddressField(null=True, blank=True)

    object = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        # Generate UID
        if not self.uid:
            from core.core.generator import generate_id
            self.uid = generate_id('account')
        if self.phone:
            from core.core.normalization import normalize_phone
            cleaned_phone = normalize_phone(self.phone)
            if cleaned_phone is not None:
                self.phone = cleaned_phone
            else:
                self.phone = None
        super(Account, self).save(*args, **kwargs)





