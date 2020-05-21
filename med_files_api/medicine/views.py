from core.views import BaseMedFileViewSet

from .models import Medicine
from .serializers import MedicineSerializer


class MedicineViewSet(BaseMedFileViewSet):
    """
    CRUD options for medicine only for authenticated user.
    """
    serializer_class = MedicineSerializer
    queryset = Medicine.objects.all()
