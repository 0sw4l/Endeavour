from django.db import models
from Apps.Users.models import Cliente
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
    precio = models.PositiveIntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="endeavour")
    usado = models.BooleanField(default=False)
    eliminado = models.BooleanField(default=False, editable=False)
    voto_positivo = models.IntegerField(default=0, editable=False)
    voto_negativo = models.IntegerField(default=0, editable=False)


class ComentarioProducto(models.Model):

    producto = models.ForeignKey(Producto)
    cliente = models.ForeignKey(Cliente)
    comentario = models.TextField()

