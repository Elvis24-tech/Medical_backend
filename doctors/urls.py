from rest_framework.routers import (
    DefaultRouter
)

from .views import (
    DoctorViewSet,
    DoctorScheduleViewSet
)

router = (
    DefaultRouter()
)

router.register(
    "",
    DoctorViewSet
)

router.register(
    "schedule",
    DoctorScheduleViewSet
)

urlpatterns = (
    router.urls
)