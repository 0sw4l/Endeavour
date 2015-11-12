from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [

    url(r'^registro/', views.register_user, name='registro'),
    url(r'^registro-completado/', views.registro_completado, name='registro_completado'),
    url(r'^confirmar-registro/(?P<activation_key>\w+)', views.register_confirm)
]
