from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import QueryViewSet, TranslateViewSet

router = DefaultRouter()
router.register(r'api/translate-management', TranslateViewSet)
router.register(r'api/query-management', QueryViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
