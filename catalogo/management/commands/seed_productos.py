from django.core.management.base import BaseCommand
from catalogo.models import Producto


class Command(BaseCommand):
    help = "Carga productos de ejemplo en la base de datos para pruebas y demostraciones."

    def handle(self, *args, **options):
        Producto.objects.all().delete()
        productos = [
            ("Laptop Lenovo IdeaPad 3", 2899.90, "LAPTOP", 12),
            ("Laptop ASUS Vivobook 15", 3199.00, "LAPTOP", 0),
            ("iPhone 15", 4500.00, "CELULAR", 8),
            ("Samsung Galaxy A55", 1599.50, "CELULAR", 20),
            ("Mouse Logitech MX Master 3", 349.90, "PERIFERICO", 30),
            ("Teclado mecánico Redragon", 189.90, "PERIFERICO", 0),
            ("Memoria RAM Kingston 16GB", 219.00, "COMPONENTE", 45),
            ("SSD NVMe 1TB WD", 329.00, "COMPONENTE", 15),
            ("Mochila para laptop Targus", 99.90, "ACCESORIO", 25),
            ("Audífonos Bluetooth JBL", 159.90, "ACCESORIO", 0),
        ]
        for nombre, precio, categoria, stock in productos:
            Producto.objects.create(
                nombre=nombre, precio=precio, categoria=categoria, stock=stock
            )
        self.stdout.write(self.style.SUCCESS(f"Se cargaron {len(productos)} productos de ejemplo."))
