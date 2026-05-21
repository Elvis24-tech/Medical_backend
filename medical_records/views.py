from rest_framework import viewsets
from rest_framework.permissions import (
IsAuthenticated
)
from .models import (
    MedicalRecord,
    Prescription
)
from .serializers import (
    MedicalRecordSerializer,
    PrescriptionSerializer
)
class MedicalRecordViewSet(
    viewsets.ModelViewSet
):
    serializer_class = (
        MedicalRecordSerializer
    )
    permission_classes = (
        IsAuthenticated,
    )
    queryset = (
        MedicalRecord.objects.all()
    )
    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            return MedicalRecord.objects.all()
        if user.role == "doctor":
            return MedicalRecord.objects.filter(
                doctor__user=user
            )
        if user.role == "patient":
            return MedicalRecord.objects.filter(
                patient__user=user
            )

        return MedicalRecord.objects.none()
class PrescriptionViewSet(
    viewsets.ModelViewSet
):
    serializer_class = (
        PrescriptionSerializer
    )
    permission_classes = (
        IsAuthenticated,
    )
    queryset = (
        Prescription.objects.all()
    )