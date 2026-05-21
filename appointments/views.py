from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Appointment
from .serializers import AppointmentSerializer
from patients.models import Patient
from billing.models import Bill
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        if user.role == "admin":
            return Appointment.objects.all()
        elif user.role == "doctor":
            return Appointment.objects.filter(
                doctor__user=user
            )

        elif user.role == "patient":
            return Appointment.objects.filter(
                patient__user=user
            )

        return Appointment.objects.none()

    def perform_create(
        self,
        serializer
    ):

        try:

            patient = Patient.objects.get(
                user=self.request.user
            )

        except Patient.DoesNotExist:
            raise Exception(
                "Patient profile missing."
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

        appointment = self.get_object()
        if request.user.role != "doctor":
            return Response(
                {
                    "error":
                    "Only doctors can approve appointments"
                },
                status=status.HTTP_403_FORBIDDEN
            )
        if appointment.doctor.user != request.user:
            return Response(
                {
                    "error":
                    "You cannot approve another doctor's appointment"
                },
                status=status.HTTP_403_FORBIDDEN
            )

        if appointment.status == "approved":
            return Response(
                {
                    "message":
                    "Already approved"
                }
            )
        appointment.status = "approved"
        appointment.save()
        bill, created = Bill.objects.get_or_create(
            appointment=appointment,
            defaults={
                "patient":
                appointment.patient,
                "amount":
                appointment.doctor.consultation_fee,
                "description":
                (
                    f"Consultation with "
                    f"{appointment.doctor.user.username}"
                )
            }
        )
        return Response({

            "message":
            "Appointment approved",
            "bill_created":
            created,

            "bill_id":
            bill.id

        })

    @action(
        detail=True,
        methods=["post"]
    )
    def cancel(
        self,
        request,
        pk=None
    ):
        appointment = self.get_object()
        if appointment.status == "completed":
            return Response(
                {
                    "error":
                    "Completed appointments cannot be cancelled"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        appointment.status = "cancelled"
        appointment.save()
        return Response({

            "message":
            "Appointment cancelled"

        })

    @action(
        detail=True,
        methods=["post"]
    )
    def complete(
        self,
        request,
        pk=None
    ):

        appointment = self.get_object()
        if request.user.role != "doctor":
            return Response(
                {
                    "error":
                    "Only doctors can complete appointments"
                },
                status=status.HTTP_403_FORBIDDEN
            )

        appointment.status = "completed"
        appointment.save()
        return Response({
            "message":
            "Appointment completed"

        })