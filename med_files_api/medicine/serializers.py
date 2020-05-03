from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Medicine


class MedicineSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Medicine
        fields = ('id', 'name', 'user', 'description', 'med_form', 'med_type')
        validators = [
            UniqueTogetherValidator(
                queryset=Medicine.objects.all(),
                fields=['user', 'name']
            )
        ]
