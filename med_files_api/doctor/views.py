from rest_framework import viewsets, authentication, permissions
from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """This view return a list of all doctors for the currently authenticated user."""
        user = self.request.user
        return Doctor.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
