from rest_framework import serializers
from . import models


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = ('id', 'name', 'adres', 'phone_number', 'doc_type')
