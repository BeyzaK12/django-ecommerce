from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core import validators
from django.core.validators import RegexValidator

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)

    # +999999999
    # +905469692012

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Telefon numarası '+999999999' biçiminde girilmelidir. 15 haneye kadar izin verilir.\nÖrneğin: +905121231234")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # validators should be a list

    # 10000000000 - 99999999999
    kimlik_numarası = models.BigIntegerField(default=10000000000, validators=[
        validators.MinValueValidator(10000000000), validators.MaxValueValidator(99999999999)])
    vergi_numarası = models.BigIntegerField(default=1000000000, validators=[
        validators.MinValueValidator(1000000000), validators.MaxValueValidator(9999999999)])
    first_name = models.CharField(_('first name'), max_length=50, null=True)
    last_name = models.CharField(_('last name'), max_length=50, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['kimlik_numarası', 'phone_number',
                       'vergi_numarası', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
