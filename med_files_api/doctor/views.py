from rest_framework import viewsets

from .models import Doctor
from .serializers import DoctorSerializer


class DoctorsViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
