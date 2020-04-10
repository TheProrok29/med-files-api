from django.shortcuts import render
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework import viewsets


class DoctorsViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
