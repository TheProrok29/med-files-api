from .models import Doctor
from .serializers import DoctorSerializer
from core.views import BaseMedFileViewSet


class DoctorViewSet(BaseMedFileViewSet):
    """"CRUD options for Doctor for authenticated user"""
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
