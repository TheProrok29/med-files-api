from core.views import BaseMedFileViewSet

from .models import MedResult, MedImage
from .serializers import MedResultSerializer, MedImageSerializer, MedResultDetailSerializer


class MedResultViewSet(BaseMedFileViewSet):
    """
    CRUD options for med result only for authenticated user.
    """
    serializer_class = MedResultSerializer
    queryset = MedResult.objects.all()

    def get_serializer_class(self):
        """
        Return appropriate serializer class.
        """
        if self.action == 'retrieve':
            return MedResultDetailSerializer
        return self.serializer_class


class MedImageViewSet(BaseMedFileViewSet):
    """
    CRUD options for med image only for authenticated user.
    """
    serializer_class = MedImageSerializer
    queryset = MedImage.objects.all()
