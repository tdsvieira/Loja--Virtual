from django.contrib.auth.models import AbstractUser
from django.db import models


# Usuario customizado para separar cliente e vendedor
class Usuario(AbstractUser):
    TIPO_USUARIO = (
        ('cliente', 'Cliente'),
        ('vendedor', 'Vendedor'),
    )
    tipo = models.CharField(max_length=10, choices=TIPO_USUARIO, default='cliente')


class Produto(models.Model):
    vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo': 'vendedor'})
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome
