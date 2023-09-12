from django.contrib import admin
from django.urls import path, include
from tdcore import urls as tdcore_urls
from tdtaskManagement import urls as tdtaskManagement_urls
from tdauth import urls as tdauth_urls

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('todobe/admin/', admin.site.urls),
    path('todobe/api/', include(tdcore_urls)),
    path('todobe/api/', include(tdtaskManagement_urls)),
    path('todobe/api/', include(tdauth_urls)),
]

schema_view = get_schema_view(
   openapi.Info(
      title="ToDo App API",
      default_version='v1.0.0',
      description="Test description",
      terms_of_service="",
      contact=openapi.Contact(email="contact@comapany.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

swagger_urlpatterns = [
   path('todobe/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('todobe/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('todobe/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += swagger_urlpatterns