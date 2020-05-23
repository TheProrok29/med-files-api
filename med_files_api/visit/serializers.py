from core.models import Tag
from core.serializers import UserFilteredPrimaryKeyRelatedField
from doctor.models import Doctor
from doctor.serializers import DoctorSerializer
from med_result.models import MedResult
from med_result.serializers import MedResultSerializer
from medicine.models import Medicine
from medicine.serializers import MedicineSerializer
from core.serializers import TagSerializer
from rest_framework import serializers


from .models import Visit


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


class VisitDetailSerializer(VisitSerializer):
    """
    Serializer a visit detail. Show detail visit with other conencted models data
    instead of only pk.
    """
    doctor = DoctorSerializer(read_only=True)
    medicine = MedicineSerializer(many=True, read_only=True)
    med_result = MedResultSerializer(many=True, read_only=True)
    tag = TagSerializer(many=True, read_only=True)
