import os
import uuid

from django.conf import settings
from django.db import models


def exam_result_file_path(instance, filename):
    """Generate file path for new exam result image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/med_result/', filename)


class MedResult(models.Model):
    """"Model using to store medical examination result object"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Description')
    add_date = models.DateTimeField(auto_now_add=True)
    date_of_exam = models.DateTimeField()
    image = models.ImageField(null=True, blank=True, upload_to=exam_result_file_path)

    def __str__(self):
        return self.description[:100]
