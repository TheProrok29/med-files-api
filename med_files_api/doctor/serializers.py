from rest_framework import serializers

from .models import Doctor, DoctorSpecialization


class DoctorSerializer(serializers.ModelSerializer):
    """Serializer a Doctor model field"""
    class Meta:
        model = Doctor
        fields = ('id', 'name', 'adres', 'phone_number', 'specialization')


class DoctorSpecializationSerializer(serializers.ModelSerializer):
    """Serializer a DoctorSpecialization model field"""

    class Meta:
        model = DoctorSpecialization
        fields = ('id', 'name')
