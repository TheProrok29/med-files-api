from rest_framework import serializers
from .models import Medicines


class MedicinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicines
        fields = ('id', 'name', 'description', 'med_form', 'med_type')
