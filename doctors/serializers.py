from rest_framework import serializers
from .models import (
    Doctor,
    DoctorSchedule
)
class DoctorSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Doctor
        fields = "__all__"


class DoctorScheduleSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = DoctorSchedule
        fields = "__all__"