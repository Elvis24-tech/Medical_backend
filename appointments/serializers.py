from rest_framework import serializers
from datetime import date
from .models import Appointment
from doctors.models import (
    DoctorSchedule
)
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

        appt_date = attrs[
            "appointment_date"
        ]

        appt_time = attrs[
            "appointment_time"
        ]

        if appt_date < date.today():

            raise serializers.ValidationError(
                "Past dates not allowed."
            )

        if not doctor.available:

            raise serializers.ValidationError(
                "Doctor unavailable."
            )

        try:

            schedule = (
                DoctorSchedule.objects
                .get(
                    doctor=doctor
                )
            )

        except:

            raise serializers.ValidationError(
                "Doctor schedule missing."
            )

        if not (
            schedule.start_time
            <=
            appt_time
            <=
            schedule.end_time
        ):

            raise serializers.ValidationError(
                "Outside schedule."
            )

        exists = (
            Appointment.objects
            .filter(
                doctor=doctor,
                appointment_date=appt_date,
                appointment_time=appt_time
            )
            .exists()
        )

        if exists:

            raise serializers.ValidationError(
                "Slot already booked."
            )

        return attrs