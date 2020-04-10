from django.shortcuts import render
from . import models
from . import serializers


class DoctorViewset(viewsets.ModelViewSet):
    quaryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
