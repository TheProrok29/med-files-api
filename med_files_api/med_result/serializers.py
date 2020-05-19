from rest_framework import serializers
from visit.serializers import UserFilteredPrimaryKeyRelatedField
from .models import MedResult, MedImage
from core.models import Tag


class MedResultSerializer(serializers.ModelSerializer):
    """Serializer a med result detail"""
    tag = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    images = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='api:med_image-detail')

    class Meta:
        model = MedResult
        fields = ('id', 'name', 'description', 'add_date', 'date_of_exam', 'images', 'tag')
        read_only_fields = ('id',)


class MedImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to med results"""
    med_result = UserFilteredPrimaryKeyRelatedField(queryset=MedResult.objects)

    class Meta:
        model = MedImage
        fields = ('id', 'name', 'image', 'med_result')
