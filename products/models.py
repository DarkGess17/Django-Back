from django.db import models

#Modelo de Categorias

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    image = models.ImageField(upload_to='products', default='default.png', verbose_name='Imagen')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_products', verbose_name='Categoria')
    description = models.TextField(verbose_name='Descripcion')
    calification = models.DecimalField (max_digits=3, decimal_places=1, null=True, verbose_name='Calificacion')
    price = models.DecimalField (max_digits=10, decimal_places=0, verbose_name='Precio')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['name']

    def __str__(self):
        return self.name