from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=5, default='0')
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=14)
    grupoacesso = models.CharField(
        max_length=50,
        choices=[
            ('importacao', 'Importação'),
            ('usuario', 'Usuário'),
            ('administrador', 'Administrador'),
        ],
        default='importacao'
    )
    observacoes = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.user.username
