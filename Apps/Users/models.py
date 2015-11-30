from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Trabajador(User):
    pass


class Cliente(User, models.Model):

    token = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Clientes'