from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ImageInfoViewSet

router = DefaultRouter()
router.register(r'api/image-management', ImageInfoViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
