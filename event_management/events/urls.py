from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EventRegistrationViewSet, EventViewSet

router = DefaultRouter()
router.register(r"events", EventViewSet)
router.register(r"registrations", EventRegistrationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
