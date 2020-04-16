from rest_framework import viewsets

from .models import Medicine
from .serializers import MedicineSerializer


class MedicinesViewSet(viewsets.ModelViewSet):
    serializer_class = MedicineSerializer
    queryset = Medicine.objects.all()
