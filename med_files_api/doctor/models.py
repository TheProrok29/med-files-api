from django.db import models
from django.conf import settings


class DoctorSpecialization(models.Model):
    """DoctorSpecialization model that be using during creating a new doctor"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    """"Model using to store medical examination result object"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=120, unique=True)
    adres = models.CharField(verbose_name='Adres', max_length=200, blank=True, null=True)

    phone_number = models.CharField(
        verbose_name='Phone Number', max_length=12, blank=True, null=True)

    specialization = models.ForeignKey('DoctorSpecialization', verbose_name='Specialization', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
