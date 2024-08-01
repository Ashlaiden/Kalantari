import uuid
from datetime import datetime

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
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


class AddressManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

    def get_user_addresses(self, user_id=None, user=None):
        try:
            queryset = self.get_queryset()
            if user_id is not None:
                queryset = queryset.filter(user_id=user_id)
            if user is not None:
                queryset = queryset.filter(user=user)
            return queryset.all()
        except BaseException:
            return None

    def get_user_address_count(self, user_id=None, user=None):
        try:
            queryset = self.get_queryset()
            if user_id is not None:
                queryset = queryset.filter(user_id=user_id)
            elif user is not None:
                queryset = queryset.filter(user=user)
            else:
                queryset = []
            return queryset.all().count()
        except BaseException:
            return None

    def unique_address_title(self, name, user_id=None, user=None):
        try:
            queryset = self.get_queryset()
            if user_id is not None:
                queryset = queryset.filter(user_id=user_id)
            elif user is not None:
                queryset = queryset.filter(user=user)
            else:
                queryset = []
            for address in queryset:
                if address.title == name:
                    return False
            return True
        except BaseException:
            return None

    def get_address(self, item_id, user_id=None, user=None):
        try:
            if user_id is not None:
                data = self.get_queryset().filter(pk=item_id, user_id=user_id)
            elif user is not None:
                data = self.get_queryset().filter(pk=item_id, user=user)
            else:
                data = self.get_queryset().filter(pk=item_id)
            return data
        except BaseException:
            return None


class Account(AbstractBaseUser, PermissionsMixin):
    uid = models.IntegerField(null=False, editable=False, unique=True)
    # Add your custom fields here
    email = models.EmailField(unique=True, null=False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(validators=[RegexValidator(regex=r'^\+\d{1,3}9\d{9}$')], max_length=15, null=False, blank=False)
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

    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id'])
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        # Generate UID
        from core.core.generator import generate_uid
        self.uid = generate_uid('account')
        if self.phone:
            from core.core.normalization import normalize_phone
            cleaned_phone = normalize_phone(self.phone)
            if cleaned_phone is not None:
                self.phone = cleaned_phone
            else:
                self.phone = None
        super(Account, self).save(*args, **kwargs)


class Address(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='addresses')
    title = models.CharField(max_length=50, blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    j_created = jmodels.jDateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    address_manager = AddressManager()

    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id'])
        ]

    def __str__(self):
        return f'{self.user.uid}--{self.user.first_name} {self.user.last_name}--[{self.title}]'

