from rest_framework import serializers

from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    """Serializer a Doctor model fields"""
    class Meta:
        model = Doctor
        fields = ('id', 'name', 'adres', 'phone_number', 'specialization')
