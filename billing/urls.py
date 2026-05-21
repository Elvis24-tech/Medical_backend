from rest_framework.routers import (
    DefaultRouter
)
from .views import (
    BillViewSet
)
router = (
    DefaultRouter()
)
router.register(
    "",
    BillViewSet,
    basename="billing"
)
urlpatterns = (
    router.urls
)