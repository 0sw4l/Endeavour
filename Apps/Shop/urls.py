__author__ = 'osw4l'
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^buy/(?P<producto>\w+)/', views.comprar, name='comprar'),
]
