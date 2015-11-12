from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView
from forms import CategoriaForm, ProductoForm
from  .models import Categoria, Producto
# Create your views here.


@login_required
def crear_producto(request):
    form = ProductoForm()
    if request.POST:
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    context = {
        'form': form
    }
    return render(request, 'producto_form.html', context)


@login_required
def crear_categoria(request):
    form = CategoriaForm()
    if request.POST:
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    return render(request, 'categoria_form.html', {'form': form})


@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'list_productos.html', context)


class ProductosView(ListView):

    template_name = 'list_productos.html'
    model = Producto
    paginate_by = 10


class CategoriasView(ListView):

    template_name = 'list_categorias.html'
    model = Categoria
    paginate_by = 10


@login_required
def editar_producto(request, **kwargs):

    id = kwargs.get('pk')
    producto = Producto.objects.get(id=id)
    form = ProductoForm(instance=producto)
    if request.POST:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    context = {
         'form': form
    }
    return render(request, 'producto_form.html', context)


@login_required
def editar_categoria(request, **kwargs):
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
