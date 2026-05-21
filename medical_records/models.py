from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="medical_records"
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE
    )

    diagnosis = models.TextField()
    symptoms = models.TextField()
    treatment = models.TextField()
    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return (
            f"{self.patient.user.username}"
            f" - "
            f"{self.diagnosis}"
        )


class Prescription(models.Model):
    medical_record = models.ForeignKey(
        MedicalRecord,
        on_delete=models.CASCADE,
        related_name="prescriptions"
    )
    medication_name = models.CharField(
        max_length=255
    )
    dosage = models.CharField(
        max_length=255
    )
    frequency = models.CharField(
        max_length=255
    )
    duration = models.CharField(
        max_length=255
    )
    instructions = models.TextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.medication_name