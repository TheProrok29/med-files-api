from django.shortcuts import render
from .models import Medicine
from .serializers import MedicineSerializer
from rest_framework import viewsets


class MedicinesViewSet(viewsets.ModelViewSet):
    serializer_class = MedicineSerializer
    queryset = Medicine.objects.all()
