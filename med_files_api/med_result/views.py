from core.views import BaseMedFileViewSet

from .models import MedResult, MedImage
from .serializers import MedResultSerializer, MedImageSerializer


class MedResultViewSet(BaseMedFileViewSet):
    """
    CRUD options for med result only for authenticated user.
    """
    serializer_class = MedResultSerializer
    queryset = MedResult.objects.all()


class MedImageViewSet(BaseMedFileViewSet):
    """
    CRUD options for med image only for authenticated user.
    """
    serializer_class = MedImageSerializer
    queryset = MedImage.objects.all()
