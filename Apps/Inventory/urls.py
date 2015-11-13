__author__ = 'osw4l'
from django.contrib.auth.decorators import login_required
from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^new-product/$', views.crear_producto, name='crear_producto'),
    url(r'^new-category/$', views.crear_categoria, name='crear_categoria'),
    url(r'^new-type/$', views.crear_tipo_producto, name='crear_tipo_producto'),

    url(r'^list-products/$', login_required(views.ProductosView.as_view()), name='lista_productos'),
    url(r'^list-categories/$', login_required(views.CategoriasView.as_view()), name='lista_categorias'),
    url(r'^list-types/$', login_required(views.TiposProductoView.as_view()), name='lista_tipos'),

    url(r'^modify-product/(?P<pk>\d+)/$', views.editar_producto, name='editar_producto'),
    url(r'^modify-category/(?P<pk>\d+)/$', views.editar_categoria, name='editar_categoria'),
    url(r'^modify-type/(?P<pk>\d+)/$', views.editar_tipo_producto, name='editar_tipo'),

]
