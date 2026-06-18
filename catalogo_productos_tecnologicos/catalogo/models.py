from django.db import models


class Producto(models.Model):
    """
    Modelo que representa un producto tecnológico dentro del catálogo.
    Cumple con el mínimo de 4 campos solicitado en la guía:
    nombre, precio, categoria y stock (más creado_en como campo de auditoría).
    """

    CATEGORIA_CHOICES = [
        ('LAPTOP', 'Laptops'),
        ('CELULAR', 'Celulares'),
        ('PERIFERICO', 'Periféricos'),
        ('COMPONENTE', 'Componentes'),
        ('ACCESORIO', 'Accesorios'),
    ]

    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, default='ACCESORIO')
    stock = models.PositiveIntegerField(default=0)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Productos"
        ordering = ["-creado_en"]

    def __str__(self):
        # Representación legible en el admin y en el shell de Django.
        return f"{self.nombre} (S/ {self.precio})"

    @property
    def disponible(self):
        """Atributo de conveniencia usado en plantillas para el condicional de stock."""
        return self.stock > 0
