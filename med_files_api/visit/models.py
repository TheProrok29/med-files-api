# from django.db import models
# from django.conf import settings
# from medicine.models import Medicine
# from doctor.models import Doctor
# from med_result.models import MedResult


# class Visit(models.Model):
#     """A model that represents a medical visit and integrates
#     most of the other modules"""

#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     visit_date = models.DateTimeField()
#     doctor = models.ForeignKey(Doctor)
#     medicine = models.ForeignKey(Medicine, blank=True, null=True)
#     med_result = models.ForeignKey(MedResult, blank=True, null=True)
