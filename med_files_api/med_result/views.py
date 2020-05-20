from core.views import BaseMedFileViewSet

from .models import MedResult, MedImage
from .serializers import MedResultSerializer, MedImageSerializer


class MedResultViewSet(BaseMedFileViewSet):
    serializer_class = MedResultSerializer
    queryset = MedResult.objects.all()


class MedImageViewSet(BaseMedFileViewSet):
    serializer_class = MedImageSerializer
    queryset = MedImage.objects.all()
