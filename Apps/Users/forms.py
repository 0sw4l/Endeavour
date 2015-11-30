# coding=utf-8
from django.contrib.auth import authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from Apps.Users.models import Cliente


class EmailAuthenticationForm(forms.Form):

    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    administrador = False

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):

        super(EmailAuthenticationForm, self).clean()

        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        self.user_cache = authenticate(email=email, password=password)

        if self.user_cache is None:
            self._errors["email"] = self.error_class(['Usuario o Password incorrecta'])
        elif not self.user_cache.is_active:
            self._errors["email"] = self.error_class(['Usuario Inactivo'])

        return self.cleaned_data

    def get_user(self):
        return self.user_cache

    def is_admin(self):
        return self.user_cache.is_superuser


class ClienteForm(UserCreationForm):

    class Meta:
        model = Cliente
        fields = ['first_name', 'last_name', 'email']
