import hashlib
import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout
# Create your views here.
from Apps.Users.forms import EmailAuthenticationForm,  ClienteForm
from models import Cliente
from Mails import enviar_token


def signin(request):
    if not request.user.is_anonymous():
        return redirect('inicio')
    else:
        form = EmailAuthenticationForm(request.POST or None)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if form.is_admin():
                return redirect('lista_productos')
            else:
                return redirect('inicio')
    return render(request, 'login.html', {'form': form})


@login_required
def log_out(request):
    logout(request)
    return redirect('inicio')


def register_user(request):
    form = ClienteForm()
    if request.POST:
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.instance
            cliente = Cliente.objects.get(email=data.email)
            cliente.username = data.email
            cliente.is_active = False
            key = hashlib.sha1(str(random.random())).hexdigest()[:5]
            cliente.activation_key = hashlib.sha1(key+data.email).hexdigest()
            cliente.save()

            data_mail = {
                'nombre': "{0} {1}".format(data.first_name, data.last_name),
                'email': data.email,
                'token': cliente.activation_key
            }

            enviar_token(**data_mail)
            return redirect('registro_completado')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def registro_completado(request):
    return render(request, 'completado.html')


def register_confirm(request, token):
    if request.user.is_authenticated():
        return redirect('inicio')
    else:
        user = None
        try:
            user = Cliente.objects.get(token=token)
            if not user.is_active:
                user.is_active = True
                user.save()
                return redirect('success', user.first_name)
            else:
                return redirect('entrar')
        except Cliente.DoesNotExist:
            return render(request, 'clave_no_existe.html')


def success(request, user):
    return render(request, 'confirmado.html', {
        'user': user
    })
