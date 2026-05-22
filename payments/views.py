from uuid import uuid4
from rest_framework import (
    viewsets,
    status
)
from rest_framework.decorators import (
    action
)
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework.response import (
    Response
)
from .models import Payment
from .serializers import PaymentSerializer
class PaymentViewSet(
    viewsets.ModelViewSet
):
    queryset = (
        Payment.objects.all()
    )
    serializer_class = (
        PaymentSerializer
    )
    permission_classes = (
        IsAuthenticated,
    )
    def get_queryset(
        self
    ):
        user = self.request.user
        if user.role == "admin":
            return Payment.objects.all()
        return Payment.objects.filter(
            bill__patient__user=user
        )

    @action(
        detail=True,
        methods=["post"]
    )
    def pay(
        self,
        request,
        pk=None
    ):

        payment = self.get_object()
        if payment.bill.paid:
            return Response(
                {
                    "message":
                    "Bill already paid"
                }
            )
        payment.transaction_id = (
            str(uuid4())[:12]
        )
        payment.status = (
            "completed"
        )
        payment.save()
        bill = payment.bill
        bill.paid = True
        bill.save()
        return Response(
            {
                "message":
                "Payment successful",
                "transaction_id":
                payment.transaction_id
            },
            status=status.HTTP_200_OK
        )