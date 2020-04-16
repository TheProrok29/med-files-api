from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from .serializers import UserSerializer
from core.models import User


class CreateUserView(CreateModelMixin, viewsets.GenericViewSet):
    """Create a new user in the system"""
    model = User
    serializer_class = UserSerializer
