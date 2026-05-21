from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Appointment
from .serializers import AppointmentSerializer
from patients.models import Patient
class AppointmentViewSet(
    viewsets.ModelViewSet
):

    serializer_class = (
        AppointmentSerializer
    )

    permission_classes = (
        IsAuthenticated,
    )

    queryset = (
        Appointment.objects
        .all()
    )

    def perform_create(
        self,
        serializer
    ):

        patient = Patient.objects.get(
            user=self.request.user
        )

        serializer.save(
            patient=patient
        )

    def get_queryset(
        self
    ):

        user = self.request.user
        if user.role == "admin":
            return Appointment.objects.all()
        if user.role == "doctor":
            return Appointment.objects.filter(
                doctor__user=user
            )

        if user.role == "patient":
            return Appointment.objects.filter(
                patient__user=user
            )
        return Appointment.objects.none()