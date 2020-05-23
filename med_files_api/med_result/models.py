import os
import uuid

from core.models import Tag
from visit.models import Visit
from django.conf import settings
from django.db import models


def med_image_file_path(instance, filename):
    """
    Generate file path for new med image.
    """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('uploads/med_result/', filename)


class MedResult(models.Model):
    """
    Model using to store medical result object.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=255)
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    add_date = models.DateField(auto_now_add=True)
    date_of_exam = models.DateField(null=True, blank=True)
    visit = models.ForeignKey(Visit, null=True, blank=True, on_delete=models.SET_NULL, related_name='med_result')
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class MedImage(models.Model):
    """
    Model using to collect medical image.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to=med_image_file_path)
    med_result = models.ForeignKey(MedResult, null=True, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.name
