from rest_framework import (
    viewsets,
    status
)
from rest_framework.decorators import (
    action
)
from rest_framework.response import (
    Response
)
from rest_framework.permissions import (
    IsAuthenticated
)
from .models import Appointment
from .serializers import (
    AppointmentSerializer
)
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
        Appointment.objects.all()
    )

    def get_queryset(self):
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
    def perform_create(
        self,
        serializer
    ):

        patient = (
            Patient.objects.get(
                user=self.request.user
            )
        )

        serializer.save(
            patient=patient,
            status="pending"
        )

    @action(
        detail=True,
        methods=["post"]
    )
    def approve(
        self,
        request,
        pk=None
    ):

        appointment = (
            self.get_object()
        )

        if (
            request.user.role
            !=
            "doctor"
        ):

            return Response(
                {
                    "error":
                    "Only doctors can approve"
                },
                status=403
            )

        appointment.status = (
            "approved"
        )

        appointment.save()
        return Response(
            {
                "message":
                "Appointment approved"
            }
        )

    @action(
        detail=True,
        methods=["post"]
    )
    def cancel(
        self,
        request,
        pk=None
    ):

        appointment = (
            self.get_object()
        )

        appointment.status = (
            "cancelled"
        )

        appointment.save()
        return Response(
            {
                "message":
                "Appointment cancelled"
            }
        )