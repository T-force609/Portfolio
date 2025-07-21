from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from portfolio_app.views import ContactRequestViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contact_request', ContactRequestViewSet, basename='contact_request')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom_admin/', include('custom_admin.urls')),
    path('api/', include('portfolio_app.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
