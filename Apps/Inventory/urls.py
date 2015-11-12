__author__ = 'osw4l'
from django.contrib.auth.decorators import login_required
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^nuevo-producto/$', views.crear_producto, name='crear_producto'),
    url(r'^nueva-categoria/$', views.crear_categoria, name='crear_categoria'),
    url(r'^lista-productos/$', login_required(views.ProductosView.as_view()), name='lista_productos'),
    url(r'^lista-categorias/$', login_required(views.CategoriasView.as_view()), name='lista_categorias'),
    url(r'^editar-producto/(?P<pk>\d+)/$', views.editar_producto, name='editar_producto'),
    url(r'^editar-categoria/(?P<pk>\d+)/$', views.editar_categoria, name='editar_categoria'),
]