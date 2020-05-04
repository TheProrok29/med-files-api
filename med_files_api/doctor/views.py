from rest_framework import viewsets, authentication, permissions
from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    """"CRUD options for Doctor for authenticated user"""
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """This view return a list of all doctors for the currently authenticated user"""
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Auto add current user to serializer user field"""
        serializer.save(user=self.request.user)
