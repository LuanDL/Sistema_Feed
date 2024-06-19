from django.db import models
from usuarios.models import User
from maquinas.models import Maquinas

class Locais(models.Model):
    # usuario = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    local = models.CharField(max_length=100)
    maquina = models.ForeignKey(Maquinas, on_delete=models.CASCADE)

def __str__(self):
    return self.local