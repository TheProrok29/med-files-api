from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MedicinesSerializer
from .models import Medicines


class MedicinesView(viewsets.ModelViewSet):
    serializer_class = MedicinesSerializer
    queryset = Medicines.objects.all()
