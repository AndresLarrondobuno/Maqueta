from django.contrib import admin
from django.urls import re_path, include

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^recetas/', include('recetas.urls')),
    re_path(r'^cuentas/', include('cuentas.urls')),
]
