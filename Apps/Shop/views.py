from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView
from Apps.Inventory.models import Producto
from Apps.Inventory.models import ComentarioProducto
# Create your views here.
from Apps.Shop.models import Pedido


@login_required
def comprar(request, **kwargs):

    id = kwargs.get('producto')
    error = False
    mensaje = ''
    producto = Producto.objects.get(id=id)
    if request.POST:
        if request.POST.get(u'compra'):
            credito_cliente = request.user.cliente.credito
            cantidad = int(request.POST.get('cantidad'))
            total = cantidad * producto.precio
            user = request.user.cliente
            if credito_cliente >= total:
                if producto.cantidad > 0 and not producto.eliminado:
                    Pedido.objects.create(
                        cliente=user,
                        producto=producto,
                        cantidad=cantidad,
                        total=total,
                    )
                    user.credito -= total
                    user.save()
                    return redirect('exitoso')
                else:
                    mensaje = 'El producto no esta disponible'
                    error = True
            else:
                mensaje = 'No tiene credito suficiente para realizar esta compra'
                error = True
    context = {
        'producto': producto,
        'error': error,
        'mensaje': mensaje
    }
    return render(request, 'shop_product.html', context)


@login_required
def pedido_exitoso(request):
    pedido = Pedido.objects.filter(cliente=request.user.cliente).last()
    return render(request, 'exitoso.html', {
        'pedido': pedido
    })


@login_required
def pedido_cliente_detalle(request, **kwargs):
    id = kwargs.get('pedido')
    pedido = Pedido.objects.get(id=id)
    return render(request, 'detalle.html', {
        'pedido': pedido
    })


class PedidoBaseView(TemplateView):

    titulo = ''
    template_name = 'lista_de_pedidos.html'
    paginate_by = 10
    model = Pedido

    def get_context_data(self, **kwargs):
        context = super(PedidoBaseView, self).get_context_data(**kwargs)
        return context


class PedidosView(PedidoBaseView):

    titulo = 'Todos los Pedidos'

    def get_context_data(self, **kwargs):
        context = super(PedidosView, self).get_context_data(**kwargs)
        context['pedidos'] = self.model.objects.filter(cliente=self.request.user.cliente).order_by('-id')
        return context


class PedidosCanceladosView(PedidoBaseView):

    titulo = 'Cancelados'

    def get_context_data(self, **kwargs):
        context = super(PedidosCanceladosView, self).get_context_data(**kwargs)
        context['titulo'] = self.titulo
        context['pedidos'] = self.model.objects.filter(cliente=self.request.user.cliente, estado=False).order_by('-id')
        return context


class PedidosPagadosView(PedidoBaseView):

    titulo = 'Pagados'

    def get_context_data(self, **kwargs):
        context = super(PedidosPagadosView, self).get_context_data(**kwargs)
        context['titulo'] = self.titulo
        context['pedidos'] = self.model.objects.filter(
            cliente=self.request.user.cliente,
            pagado=True,
            estado=True).order_by('-id')
        return context


class PedidosNoPagadosView(PedidoBaseView):

    titulo = 'No pagados'

    def get_context_data(self, **kwargs):
        context = super(PedidosNoPagadosView, self).get_context_data(**kwargs)
        context['titulo'] = self.titulo
        context['pedidos'] = self.model.objects.filter(
            cliente=self.request.user.cliente,
            pagado=False,
            estado=True).order_by('-id')
        return context


@login_required
def cancelar_pedido(request, **kwargs):
    id = kwargs.get('pedido')
    pedido = Pedido.objects.get(id=id)
    pedido.estado = False
    pedido.save()
    user = request.user.cliente
    user.credito += pedido.total
    user.save()
    return redirect('mis_pedidos')


