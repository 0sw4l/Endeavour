from django.db import models

# Create your models here.


class Categoria(models.Model):

    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre


class TipoProducto(models.Model):

    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre


class Producto(models.Model):

    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria)
    tipo = models.ForeignKey(TipoProducto)
    cantidad = models.PositiveIntegerField()
    precio = models.FloatField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="endeavour")
    usado = models.BooleanField(default=False)
    eliminado = models.BooleanField(default=False, editable=False)



