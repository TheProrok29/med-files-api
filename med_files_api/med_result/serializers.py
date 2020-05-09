from rest_framework import serializers

from .models import MedResult
from core.models import Tag


class MedResultSerializer(serializers.ModelSerializer):
    """Serializer a med result detail"""
    tag = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = MedResult
        fields = ('id', 'name', 'description', 'add_date', 'date_of_exam', 'image', 'tag')
        read_only_fields = ('image',)


class MedResultImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to med results"""
    class Meta:
        model = MedResult
        fields = ('id', 'image')
        read_only_fields = ('id',)
