from .models import Medicine
from .serializers import MedicineSerializer
from core.views import BaseMedFileViewSet


class MedicineViewSet(BaseMedFileViewSet):
    """"CRUD options for Medicine for authenticated user"""
    serializer_class = MedicineSerializer
    queryset = Medicine.objects.all()
