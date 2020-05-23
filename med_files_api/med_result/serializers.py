from core.models import Tag
from rest_framework import serializers
from core.serializers import UserFilteredPrimaryKeyRelatedField
from core.serializers import TagSerializer
from visit.models import Visit
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
    visit = UserFilteredPrimaryKeyRelatedField(required=False, queryset=Visit.objects)

    class Meta:
        model = MedResult
        fields = ('id', 'name', 'description', 'add_date', 'date_of_exam', 'images', 'visit', 'tag')
        read_only_fields = ('id',)


class MedResultDetailSerializer(MedResultSerializer):
    """
    Serializer a med result detail. Show detail med_result with other conencted models data
    instead of only pk.
    """
    tag = TagSerializer(many=True, read_only=True)
    images = MedImageSerializer(many=True, read_only=True)
