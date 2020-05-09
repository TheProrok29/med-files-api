from rest_framework import serializers
from .models import Visit
from core.models import Tag
from medicine.models import Medicine
from doctor.models import Doctor
from med_result.models import MedResult


class UserFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(UserFilteredPrimaryKeyRelatedField, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(user=request.user)


class VisitSerializer(serializers.ModelSerializer):
    """Serializer a Visit model"""
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    doctor = UserFilteredPrimaryKeyRelatedField(queryset=Doctor.objects)
    medicine = serializers.PrimaryKeyRelatedField(many=True, queryset=Medicine.objects.all())
    med_result = serializers.PrimaryKeyRelatedField(many=True, queryset=MedResult.objects.all())
    tag = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = Visit
        fields = ('id', 'user', 'name', 'visit_date', 'adres', 'doctor', 'medicine', 'med_result', 'tag')
