from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MedicineSerializer
from .models import Medicine


class MedicinesView(viewsets.ModelViewSet):
    serializer_class = MedicineSerializer
    queryset = Medicine.objects.all()
