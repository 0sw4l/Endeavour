from django.contrib import admin
from models import Categoria, Producto
# Register your models here.


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass