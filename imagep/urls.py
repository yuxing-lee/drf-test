from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ImageInfoViewSet, ImageProcessViewSet, ImageView

router = DefaultRouter()
router.register(r'api/image-management', ImageInfoViewSet)
router.register(r'api/image-process', ImageProcessViewSet, basename="image-process")

urlpatterns = [
    path("image/", ImageView.as_view()),
    path(r'', include(router.urls)),
]
