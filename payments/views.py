from uuid import uuid4
from rest_framework import (
    viewsets
)
from rest_framework.decorators import (
    action,
    api_view
)
from rest_framework.response import (
    Response
)
from rest_framework.permissions import (
    IsAuthenticated
)
from .models import Payment
from .serializers import (
    PaymentSerializer
)
from .services.mpesa import (
    stk_push
)
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
    @action(
        detail=True,
        methods=["post"]
    )
    def stk(
        self,
        request,
        pk=None
    ):
        payment = (
            self.get_object()
        )
        result = (
            stk_push(
                payment.phone_number,
                payment.amount
            )
        )
        return Response(
            result
        )


@api_view(
    ["POST"]
)
def mpesa_callback(
    request
):
    callback = (
        request.data
    )
    try:
        checkout = (
            callback
            ["Body"]
            ["stkCallback"]
        )
        if (
            checkout
            ["ResultCode"]
            == 0
        ):
            Payment.objects.filter(
                status="pending"
            ).update(
                status=
                "completed",

            )

    except:

        pass

    return Response(
        {
            "success":
            True
        }
    )