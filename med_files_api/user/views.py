from core.models import User
from rest_framework import mixins, viewsets, authentication, permissions, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import AuthTokenSerializer, UserDataSerializer


class CreateUserView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Create a new user view.
    """
    model = User
    serializer_class = UserDataSerializer


class CreateTokenView(ObtainAuthToken):
    """
    Create new auth token for user view.
    """
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserDataView(generics.RetrieveUpdateAPIView):
    """
    Manage user authenitaction required data.
    """
    serializer_class = UserDataSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """
        Retrieve and return authenticated user.
        """
        return self.request.user
