from django.db import models

class Pedido(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombres = models.CharField(max_length=180)
    apellido_paterno = models.CharField(max_length=180)
    apellido_materno = models.CharField(max_length=180)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField(max_length=254)
    detalles_envio = models.TextField()

    class Meta:
        managed = True
        db_table = 'pedido'

class Articulo(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    imagen = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articulo'