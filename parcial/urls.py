from django.contrib import admin
from django.urls import path, include
from apps.cuentas.views import dashboard


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('apps.cuentas.urls')),
    path('', dashboard, name='home'),
    path('alumnos/', include('apps.alumnos.urls')),
]