from django.db import models
from Apps.Users.models import Cliente
from Apps.Inventory.models import Producto
# Create your models here.


class Pedido(models.Model):

    cliente = models.ForeignKey(Cliente)
    fecha = models.DateField(auto_now=True)


class PedidoDetalle(models.Model):

    producto = models.ForeignKey(Producto)
    cantidad = models.PositiveIntegerField()

