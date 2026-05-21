from rest_framework import serializers
from .models import (
    MedicalRecord,
    Prescription
)
class PrescriptionSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Prescription
        fields = "__all__"


class MedicalRecordSerializer(
    serializers.ModelSerializer
):

    prescriptions = (
        PrescriptionSerializer(
            many=True,
            read_only=True
        )
    )

    class Meta:
        model = MedicalRecord
        fields = "__all__"