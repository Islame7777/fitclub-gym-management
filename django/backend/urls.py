from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Inclut toutes tes routes de core
    path('api/', include('core.urls')),

    # inclut stripe/payments
    path('api/', include('payments.urls')),
]