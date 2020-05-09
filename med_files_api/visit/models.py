from core.models import Tag
from django.conf import settings
from django.db import models
from doctor.models import Doctor
from med_result.models import MedResult
from medicine.models import Medicine


class Visit(models.Model):
    """A model that represents a medical visit and integrates
    most of the other modules"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    visit_date = models.DateField(blank=True)
    name = models.CharField(verbose_name='Name', max_length=200)
    adres = models.CharField(verbose_name='Adres', max_length=200, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    medicine = models.ForeignKey(Medicine, blank=True, null=True, on_delete=models.SET_NULL)
    med_result = models.ForeignKey(MedResult, blank=True, null=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name
