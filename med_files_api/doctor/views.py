from rest_framework import viewsets, authentication, permissions
from .models import Doctor, DoctorSpecialization
from .serializers import DoctorSerializer, DoctorSpecializationSerializer


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
        serializer.save(user=self.request.user)


class DoctorSpecializationViewSet(viewsets.ModelViewSet):
    """"CRUD options for Doctor Specialization for authenticated user"""
    serializer_class = DoctorSpecializationSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = DoctorSpecialization.objects.all()

