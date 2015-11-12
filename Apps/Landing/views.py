from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView
from Apps.Inventory.models import Producto, Categoria

# Create your views here.


class HomeView(ListView):

    template_name = 'index.html'
    model = Producto
    paginate_by = 30
    queryset = Producto.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['productos'] = Producto.objects.count()
        context['categorias'] = Categoria.objects.count()
        return context


def log_in(request):
    context = {'error': False}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('inicio')
            else:
                context = {'msj': 'El usuario ha sido desactivado', 'error': True}
        else:
            context = {'msj': 'Usuario o Password incorrecta', 'error': True}
    return render(request, 'login.html', context)


@login_required
def log_out(request):
    logout(request)
    return redirect('inicio')

