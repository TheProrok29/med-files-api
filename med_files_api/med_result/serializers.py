from core.models import Tag
from rest_framework import serializers
from visit.serializers import UserFilteredPrimaryKeyRelatedField
from core.serializers import TagSerializer
from .models import MedResult, MedImage


class MedImageSerializer(serializers.ModelSerializer):
    """
    Serializer a med image model.
    """
    med_result = UserFilteredPrimaryKeyRelatedField(queryset=MedResult.objects)

    class Meta:
        model = MedImage
        fields = ('id', 'name', 'image', 'med_result')
        read_only_fields = ('id',)


class MedResultSerializer(serializers.ModelSerializer):
    """
    Serializer a med result model. Show connected med images.
    """
    tag = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    images = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='api:med_image-detail')

    class Meta:
        model = MedResult
        fields = ('id', 'name', 'description', 'add_date', 'date_of_exam', 'images', 'tag')
        read_only_fields = ('id',)


class MedResultDetailSerializer(MedResultSerializer):
    """
    Serializer a med result detail. Show detail med_result with other conencted models data
    instead of only pk.
    """
    tag = TagSerializer(many=True, read_only=True)
    images = MedImageSerializer(many=True, read_only=True)
