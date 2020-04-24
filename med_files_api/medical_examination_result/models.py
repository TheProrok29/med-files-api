from django.db import models
from django.conf import settings


class MedicalExaminationResult(models.Model):
    """"Model using to store medical examination result object"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Description')
    add_date = models.DateTimeField(auto_now_add=True)
    date_of_exam = models.DateTimeField()

    def __str__(self):
        return self.description[:100]
