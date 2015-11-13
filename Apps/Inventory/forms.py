__author__ = 'osw4l'
from django import forms
from .models import Categoria, Producto, TipoProducto


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ('nombre',)


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'
        exclude = ('eliminado', )


class TipoForm(forms.ModelForm):

    class Meta:
        model = TipoProducto
        fields = ('nombre', )
