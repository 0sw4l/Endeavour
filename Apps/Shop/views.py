from django.shortcuts import render
from Apps.Inventory.models import Producto
from Apps.Inventory.models import ComentarioProducto
# Create your views here.


def comprar(request, **kwargs):

    id = kwargs.get('producto')
    producto = Producto.objects.get(id=id)


    return render(request, 'shop_product.html')