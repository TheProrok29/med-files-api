from core.models import User
from rest_framework import mixins, viewsets, authentication, permissions, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import UserAuthDataSerializer, AuthTokenSerializer, UserDataSerializer


class CreateUserView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Create a new user in the system"""
    model = User
    serializer_class = UserAuthDataSerializer


class CreateTokenView(ObtainAuthToken):
    """Create new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserAuthenticationDataView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserAuthDataSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentiocated user"""
        return self.request.user


class ManageUserDataView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDataSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentiocated user"""
        return self.request.user
