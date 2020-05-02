from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Doctor(models.Model):
    """"Model using to store medical examination result object"""
    class DoctorSpecialization(models.TextChoices):
        UROLOGIS = 'URO', _('Urologis')
        ORTHOPEDIST = 'ORT', _('Orthopedist')
        OPHTHALMOLOGIST = 'OPH', _('Ophthalmologist')
        NEUROLOGIST = 'NEU', _('Neurologist')
        SURGEON = 'SUR', _('Surgeon')
        LARYNGOLOGIST = 'LAR', _('Laryngologist')
        GYNECALOGIST = 'GYN', _('Gynecologist')
        FAMILY_DOCTOR = 'FDO', _('Family doctor')
        CARDIOLOGIST = 'CAR', _('Cardiologist')
        ONCOLOGIST = 'ONC', _('Oncologist')
        GASTROENTEROLOGIST = 'GAS', _('Gastroenterologist')
        ENDYCORNOLOGIST = 'END', _('Endocrinologist.')
        DERMATOLOGIST = 'DER', _('Dermatologist')
        ALLERGIST = 'ALL', _('Allergist')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=120, unique=True)
    adres = models.CharField(verbose_name='Adres', max_length=200, blank=True, null=True)

    phone_number = models.CharField(
        verbose_name='Phone Number', max_length=12, blank=True, null=True)

    specialization = models.CharField(
        verbose_name='Specialization', max_length=3,
        choices=DoctorSpecialization.choices,
        default=DoctorSpecialization.FAMILY_DOCTOR)

    def __str__(self):
        return self.name
