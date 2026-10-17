from django.contrib.auth.models import AbstractUser
from django.db import models
from .countries import COUNTRY_CHOICES
import validators


class User(AbstractUser):
    username = models.CharField(
        max_length=11,
        unique=True,
        validators=[validators.phone_number_validators]
    )

    national_code = models.CharField(max_length=10,
        unique=True,
        validators=[validators.national_code_validators],
        blank=True,
        null=True
    )


class Passenger(models.Model):
    class Meta:
        unique_together = ('creator', 'national_code')

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="passengers")
    first_name_fa = models.CharField(
        max_length=30,
        validators=[validators.persian_name_validators]
    )
    last_name_fa = models.CharField(
        max_length=40,
        validators=[validators.persian_name_validators]
    )
    birth_date = models.DateField()
    first_name_en = models.CharField(
        max_length=30,
        validators=[validators.english_name_validators]
    )
    last_name_en = models.CharField(
        max_length=40,
        validators=[validators.english_name_validators]
    )
    gender = models.CharField(choices=[('زن', 'زن'), ('مرد', 'مرد')])
    national_code = models.CharField(
        max_length=10,
        validators=[validators.national_code_validators]
    )
    passport_number = models.CharField(max_length=15, blank=True)
    passport_expiration = models.DateField(blank=True, null=True)
    passport_country = models.CharField(max_length=30, choices=COUNTRY_CHOICES, blank=True)
    birth_country = models.CharField(max_length=30, choices=COUNTRY_CHOICES, blank=True)