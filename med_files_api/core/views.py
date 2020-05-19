from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import TagSerializer
from .models import Tag


class BaseMedFileViewSet(viewsets.ModelViewSet):
    """Base class for other views in the project permissions
    and authentication"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Automatically add the user to the new tag"""
        serializer.save(user=self.request.user)


class TagViewSet(BaseMedFileViewSet):
    """Manage tags in the database"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
