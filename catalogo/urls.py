from django.urls import path
from . import views

# Cada ruta usa 'name=' para poder referenciarla en las plantillas con
# {% url 'home' %} y {% url 'catalogo' %}, desacoplando las URLs del HTML.
urlpatterns = [
    path('', views.home, name='home'),                          # FBV bienvenida
    path('catalogo/', views.ProductoListView.as_view(), name='catalogo'),  # CBV ListView
]
