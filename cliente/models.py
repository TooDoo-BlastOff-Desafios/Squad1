from django.db import models
from uuid import uuid4


class Cliente(models.Model):
    id_usuario = models.UUIDField(auto_created=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=11, primary_key=True)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    nascimento = models.DateField()
    