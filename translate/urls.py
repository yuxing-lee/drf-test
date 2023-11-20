from django.urls import path

from .views import TranslateViewSet

urlpatterns = [
    path(r'api/translate-management', TranslateViewSet.as_view({'get': 'list'})),
]
