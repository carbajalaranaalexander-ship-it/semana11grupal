from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto


# ---------------------------------------------------------------------------
# VISTA BASADA EN FUNCIÓN (FBV)
# ---------------------------------------------------------------------------
def home(request):
    """
    Vista de bienvenida en '/'. Es una FBV simple que solo renderiza una
    plantilla estática con contexto básico (no necesita consultar el ORM).
    """
    contexto = {
        "titulo": "Catálogo de Productos Tecnológicos",
        "total_productos": Producto.objects.count(),
    }
    return render(request, "home.html", contexto)


# ---------------------------------------------------------------------------
# VISTA BASADA EN CLASE (CBV)
# ---------------------------------------------------------------------------
class ProductoListView(ListView):
    """
    CBV que lista los productos disponibles en '/catalogo/'.
    ListView ya inyecta automáticamente 'object_list' (y 'producto_list' por
    defecto), pero aquí se personaliza con context_object_name='productos'
    para que la plantilla sea más legible.
    """
    model = Producto
    template_name = "catalogo.html"
    context_object_name = "productos"

    def get_queryset(self):
        # QuerySet #1: filtra solo productos con stock disponible y los
        # ordena por precio ascendente. Es "lazy": esta línea NO consulta
        # la base de datos todavía, solo construye la consulta.
        return Producto.objects.filter(stock__gt=0).order_by('precio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # QuerySet #2: cuenta cuántos productos están agotados (stock=0).
        # Al usar .count() se fuerza la evaluación inmediata de este
        # queryset puntual, distinto al de get_queryset() que se evalúa
        # de forma diferida cuando la plantilla itera sobre 'productos'.
        context["agotados"] = Producto.objects.filter(stock=0).count()
        context["categorias"] = Producto.objects.values_list('categoria', flat=True).distinct()
        return context
