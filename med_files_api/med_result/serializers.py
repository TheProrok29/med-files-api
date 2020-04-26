from rest_framework import serializers

from .models import MedResult


class MedResultSerializer(serializers.ModelSerializer):
    """Serializer a med result detail"""
    class Meta:
        model = MedResult
        fields = ('id', 'user', 'description', 'add_date', 'date_of_exam')


class MedResultImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to med results"""
    class Meta:
        model = MedResult
        fields = ('id', 'image')
        read_only_fields = ('id',)
