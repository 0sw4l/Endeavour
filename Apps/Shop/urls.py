__author__ = 'osw4l'
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^buy/(?P<producto>\w+)/', views.comprar, name='comprar'),
    url(r'^exitoso/', views.pedido_exitoso, name='exitoso'),
    url(r'^mis-pedidos/', views.PedidosView.as_view(), name='mis_pedidos'),
    url(r'^cancelar-pedido/(?P<pedido>\w+)/', views.cancelar_pedido, name='cancelar_pedido'),
    url(r'^detalle/(?P<pedido>\w+)/', views.pedido_cliente_detalle, name='detalle_pedido'),

    url(r'^pedidos-pagados/', views.PedidosPagadosView.as_view(), name='pedidos_pagados'),
    url(r'^pedidos-cancelados', views.PedidosCanceladosView.as_view(), name='pedidos_cancelados'),
    url(r'^pedidos-no-pagados', views.PedidosNoPagadosView.as_view(), name='pedidos_no_pagados')
]
