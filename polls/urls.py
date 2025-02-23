from django.urls import path, include
from rest_framework.routers import DefaultRouter

from polls.views import HabitsViewSet, TaskViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet)
router.register(r"habits", HabitsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

