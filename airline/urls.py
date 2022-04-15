from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from bookings import urls as bookings_urls
from authentication import urls as authentication_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(authentication_urls, namespace='authentication')),
    path("", include(bookings_urls, namespace="bookings")),
]
