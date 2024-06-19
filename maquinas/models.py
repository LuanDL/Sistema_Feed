from django.db import models

selecaostatus = (
    ('A', 'ativo'),
    ('B', 'Desativado')
)

class Maquinas(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=selecaostatus)

def __str__(self):
    return self.nome
