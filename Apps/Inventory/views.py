from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from forms import CategoriaForm, ProductoForm, TipoForm
from  .models import Categoria, Producto, TipoProducto
# Create your views here.


@login_required
def crear_tipo_producto(request):
    if request.user.is_superuser:
        form = TipoForm()
        if request.POST:
            form = TipoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_tipos')
        context = {
            'form': form
        }
        return render(request, 'tipo_producto_form.html', context)
    else:
        raise PermissionDenied


@login_required
def crear_categoria(request):
    if request.user.is_superuser:
        form = CategoriaForm()
        if request.POST:
            form = CategoriaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('inicio')
        return render(request, 'categoria_form.html', {'form': form})
    else:
        raise PermissionDenied


@login_required
def crear_producto(request):
    if request.user.is_superuser:
        form = ProductoForm()
        if request.POST:
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('lista_productos')
        context = {
            'form': form
        }
        return render(request, 'producto_form.html', context)
    else:
        raise PermissionDenied


class TiposProductoView(ListView):

    template_name = 'list_tipos.html'
    model = TipoProducto
    paginate_by = 10

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise PermissionDenied
        return super(TiposProductoView, self).dispatch(*args, **kwargs)


class CategoriasView(ListView):

    template_name = 'list_categorias.html'
    model = Categoria
    paginate_by = 10

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise PermissionDenied
        return super(CategoriasView, self).dispatch(*args, **kwargs)


class ProductosView(ListView):

    template_name = 'list_productos.html'
    model = Producto
    paginate_by = 10

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise PermissionDenied
        return super(ProductosView, self).dispatch(*args, **kwargs)


@login_required
def editar_tipo_producto(request, **kwargs):
    if request.user.is_superuser:
        id = kwargs.get('pk')
        tipo = TipoProducto.objects.get(id=id)
        form = TipoForm(instance=tipo)
        if request.POST:
            form = TipoForm(request.POST, instance=tipo)
            if form.is_valid():
                form.save()
                return redirect('lista_productos')
            context = {
                'form': form
            }
        return render(request, 'tipo_producto_form.html', context)
    else:
        raise PermissionDenied


@login_required
def editar_categoria(request, **kwargs):
    if request.user.is_superuser:
        category = Categoria.objects.get(id=kwargs.get('pk'))
        form = CategoriaForm(instance=category)
        if request.POST:
            form = CategoriaForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                return redirect('lista_categorias')
        context = {
            'form': form
        }
        return render(request, 'categoria_form.html', context)
    else:
        raise PermissionDenied


@login_required
def editar_producto(request, **kwargs):
    if request.user.is_superuser:
        id = kwargs.get('pk')
        producto = Producto.objects.get(id=id)
        form = ProductoForm(instance=producto)
        if request.POST:
            form = ProductoForm(request.POST, request.FILES, instance=producto)
            if form.is_valid():
                form.save()
                return redirect('lista_productos')
        context = {
            'form': form
        }
        return render(request, 'producto_form.html', context)
    else:
        raise PermissionDenied


class DetalleProducto(DetailView):
    
    model = Producto
    template_name = 'detalle_producto.html'
    
    def get_context_data(self, **kwargs):
        context = super(DetalleProducto, self).get_context_data(**kwargs)
        context['val'] = None
        return context

    def post(self, request):
        pass
