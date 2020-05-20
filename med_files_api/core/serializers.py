from rest_framework import serializers

from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        red_only_fields = ('id',)
