from core.models import Tag
from doctor.models import Doctor
from med_result.models import MedResult
from medicine.models import Medicine
from rest_framework import serializers

from .models import Visit


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


class VisitSerializer(serializers.ModelSerializer):
    """
    Serializer a visit model.
    """
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    doctor = UserFilteredPrimaryKeyRelatedField(queryset=Doctor.objects)
    medicine = UserFilteredPrimaryKeyRelatedField(many=True, queryset=Medicine.objects)
    med_result = UserFilteredPrimaryKeyRelatedField(many=True, queryset=MedResult.objects)
    tag = UserFilteredPrimaryKeyRelatedField(many=True, queryset=Tag.objects)

    class Meta:
        model = Visit
        fields = ('id', 'user', 'name', 'visit_date', 'address', 'doctor', 'medicine', 'med_result', 'tag')
        read_only_fields = ('id',)
