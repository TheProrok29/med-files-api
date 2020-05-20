from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Tag
from .serializers import TagSerializer


class BaseMedFileViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions. This is the base
    class for other views in the project with configured permissions
    and authentication.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Return objects for the current authenticated user only.
        """
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """
        Automatically add user to the new object instance.
        """
        serializer.save(user=self.request.user)


class TagViewSet(BaseMedFileViewSet):
    """
    Manage Tags objects in the database.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
