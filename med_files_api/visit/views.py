from core.views import BaseMedFileViewSet

from .models import Visit
from .serializers import VisitSerializer


class VisitViewSet(BaseMedFileViewSet):
    """
    CRUD options for visit for authenticated user.
    """
    serializer_class = VisitSerializer
    queryset = Visit.objects.all()
