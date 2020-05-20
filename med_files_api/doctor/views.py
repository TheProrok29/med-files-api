from core.views import BaseMedFileViewSet

from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(BaseMedFileViewSet):
    """"
    CRUD options for doctor only for authenticated user.
    """
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
