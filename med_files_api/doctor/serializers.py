from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    """
    Serializer a doctor model fields with UniqueTogetherValidator for
    user and name fields.
    """
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Doctor
        fields = ('id', 'name', 'user', 'address', 'phone_number', 'specialization')
        read_only_fields = ('id',)
        validators = [
            UniqueTogetherValidator(
                queryset=Doctor.objects.all(),
                fields=['user', 'name']
            )
        ]
