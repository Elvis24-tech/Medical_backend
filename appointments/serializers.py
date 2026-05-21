from rest_framework import serializers
from datetime import date
from .models import Appointment
class AppointmentSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = (
            "patient",
        )

    def validate(
        self,
        attrs
    ):

        doctor = attrs["doctor"]
        appointment_date = attrs[
            "appointment_date"
        ]

        appointment_time = attrs[
            "appointment_time"
        ]

        if appointment_date < date.today():
            raise serializers.ValidationError(
                "Cannot book past dates."
            )

        if not doctor.available:
            raise serializers.ValidationError(
                "Doctor unavailable."
            )

        exists = Appointment.objects.filter(
            doctor=doctor,
            appointment_date=
            appointment_date,
            appointment_time=
            appointment_time

        ).exists()
        if exists:
            raise serializers.ValidationError(
                "Doctor already booked."
            )

        return attrs