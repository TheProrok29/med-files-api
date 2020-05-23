from core.views import BaseMedFileViewSet

from .models import Visit
from .serializers import VisitSerializer, VisitDetailSerializer


class VisitViewSet(BaseMedFileViewSet):
    """
    CRUD options for visit for authenticated user.
    """
    serializer_class = VisitSerializer
    queryset = Visit.objects.all()

    def get_serializer_class(self):
        """
        Return appropriate serializer class.
        """
        if self.action == 'retrieve':
            return VisitDetailSerializer
        return self.serializer_class
