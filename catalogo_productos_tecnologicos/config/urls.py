"""
config/urls.py
URLConf raíz del proyecto. Aquí solo se monta el admin y se incluye
el módulo de URLs de cada app (en este caso, 'catalogo') usando include().
Esto mantiene el enrutamiento modular: cada app gestiona sus propias rutas.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Se incluyen las URLs de la app 'catalogo' en la raíz del sitio.
    # Dentro de catalogo/urls.py se definen '/' y '/catalogo/'.
    path('', include('catalogo.urls')),
]
