from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agency.urls')),
    path('logins/', include('django.contrib.auth.urls')),
    path('logins/', include('logins.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
