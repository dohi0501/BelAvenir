
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('vih/', include('VIH.urls')),
    path('ist/', include('IST.urls')),
    path('depistage/', include('DEPISTAGE.urls')),
    path('charge_virale/', include('CHARGEVIRALE.urls')),
]
