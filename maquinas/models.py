from django.db import models

class Maquinas(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    status = models.BooleanField()

def __str__(self):
    return self.nome
