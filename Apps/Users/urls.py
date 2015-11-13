from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [

    url(r'^register/', views.register_user, name='registro'),
    url(r'^successfull-register/', views.registro_completado, name='registro_completado'),
    url(r'^confirm-user/(?P<activation_key>\w+)', views.register_confirm)
]
