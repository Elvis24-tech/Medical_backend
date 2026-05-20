from rest_framework import viewsets
from .models import Doctor
from .serializers import DoctorSerializer
from users.permissions import IsAdmin

class DoctorViewSet(viewsets.ModelViewSet):

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAdmin]