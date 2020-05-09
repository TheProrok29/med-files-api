import os
import uuid

from django.conf import settings
from django.db import models
from core.models import Tag


def med_result_file_path(instance, filename):
    """Generate file path for new med result image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/med_result/', filename)


class MedResult(models.Model):
    """"Model using to store medical examination result object"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=255)
    description = models.TextField(verbose_name='Description', blank=True)
    add_date = models.DateTimeField(auto_now_add=True)
    date_of_exam = models.DateField()
    image = models.ImageField(null=True, blank=True, upload_to=med_result_file_path)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name
