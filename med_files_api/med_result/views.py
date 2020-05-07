from rest_framework import status
from rest_framework.response import Response
from .models import MedResult
from .serializers import MedResultSerializer, MedResultImageSerializer
from rest_framework.decorators import action
from core.views import BaseMedFileViewSet


class MedResultViewSet(BaseMedFileViewSet):
    serializer_class = MedResultSerializer
    queryset = MedResult.objects.all()

    def get_serializer_class(self):
        """Return appopriate serialzier class"""
        if self.action == 'retrieve':
            return MedResultSerializer
        elif self.action == 'upload_image':
            return MedResultImageSerializer
        return self.serializer_class

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
