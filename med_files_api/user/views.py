from rest_framework import mixins, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from core.models import User

from .serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Create a new user in the system"""
    model = User
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
