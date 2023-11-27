from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="drf-test",
        default_version='v1',
        description="Welcome to the drf-test API!",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # swagger doc
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # apps
    path('', include('translate.urls')),
]
