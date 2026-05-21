from rest_framework import viewsets
from rest_framework.permissions import (
IsAuthenticated
)
from .models import (
    Doctor,
    DoctorSchedule
)

from .serializers import (
    DoctorSerializer,
    DoctorScheduleSerializer
)
class DoctorViewSet(
    viewsets.ModelViewSet
):
    queryset = (
        Doctor.objects.all()
    )
    serializer_class = (
        DoctorSerializer
    )
    permission_classes = (
        IsAuthenticated,
    )
class DoctorScheduleViewSet(
    viewsets.ModelViewSet
):
    queryset = (
        DoctorSchedule.objects.all()
    )
    serializer_class = (
        DoctorScheduleSerializer
    )
    permission_classes = (
        IsAuthenticated,
    )