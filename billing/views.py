from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated
)
from .models import Bill
from .serializers import BillSerializer
class BillViewSet(
    viewsets.ModelViewSet
):
    serializer_class = (
        BillSerializer
    )
    permission_classes = (
        IsAuthenticated,
    )
    queryset = (
        Bill.objects.all()
    )
    def get_queryset(
        self
    ):

        user = self.request.user
        if user.role == "admin":
            return Bill.objects.all()
        if user.role == "patient":
            return Bill.objects.filter(
                patient__user=user
            )
        return Bill.objects.none()