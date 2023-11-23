from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TranslateViewSet

router = DefaultRouter()
router.register(r'api/translate-management', TranslateViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
