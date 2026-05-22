from django.urls import (
    path
)
from rest_framework.routers import (
    DefaultRouter
)
from .views import (
    PaymentViewSet,
    mpesa_callback
)
router = (
    DefaultRouter()
)
router.register(
    "",
    PaymentViewSet
)
urlpatterns = [
    path(
        "callback/",
        mpesa_callback
    ),
]
urlpatterns += (
    router.urls
)