from .models import Visit
from .serializers import VisitSerializer
from core.views import BaseMedFileViewSet


class VisitViewSet(BaseMedFileViewSet):
    """"CRUD options for Medicine for authenticated user"""
    serializer_class = VisitSerializer
    queryset = Visit.objects.all()
