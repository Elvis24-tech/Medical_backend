from rest_framework.routers import (
 DefaultRouter
)
from .views import (
    MedicalRecordViewSet,
    PrescriptionViewSet
)

router = (
    DefaultRouter()
)

router.register(
    "records",
    MedicalRecordViewSet,
    basename="records"
)

router.register(
    "prescriptions",
    PrescriptionViewSet,
    basename="prescriptions"
)

urlpatterns = (
    router.urls
)