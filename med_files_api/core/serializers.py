from rest_framework import serializers

from .models import Tag


class UserFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    """
    Class filtered primary key model relation only for request.user.
    """

    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(UserFilteredPrimaryKeyRelatedField, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(user=request.user)


class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for Tag objects.
    """

    class Meta:
        model = Tag
        fields = ('id', 'name')
        red_only_fields = ('id',)
