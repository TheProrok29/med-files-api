from .models import MedResult, MedImage
from .serializers import MedResultSerializer, MedResultImageSerializer
from core.views import BaseMedFileViewSet


class MedResultViewSet(BaseMedFileViewSet):
    serializer_class = MedResultSerializer
    queryset = MedResult.objects.all()


class MedResultImageViewSet(BaseMedFileViewSet):
    serializer_class = MedResultImageSerializer
    queryset = MedImage.objects.all()
