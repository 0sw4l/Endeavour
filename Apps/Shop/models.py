from django.db import models
from Apps.Users.models import Cliente
from Apps.Inventory.models import Producto
# Create your models here.


class Pedido(models.Model):

    cliente = models.ForeignKey(Cliente)
    producto = models.ForeignKey(Producto)
    cantidad = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    fecha = models.DateField(auto_now=True)
