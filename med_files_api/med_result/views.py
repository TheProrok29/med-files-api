from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import MedResult
from .serializers import MedResultSerializer, MedResultImageSerializer
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class MedResultViewSet(viewsets.ModelViewSet):
    serializer_class = MedResultSerializer
    queryset = MedResult.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        """Rettieve the med results fot authenticated user only"""
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        """Return appopriate serialzier class"""
        if self.action == 'retrieve':
            return MedResultSerializer
        elif self.action == 'upload_image':
            return MedResultImageSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new med result"""
        serializer.save(user=self.request.user)

    @action(methods=['POST'], detail=True, url_path='upload_image')
    def upload_image(self, request, pk=None):
        """Upload an image to a med result"""
        med_result = self.get_object()
        serializer = self.get_serializer(
            med_result,
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
