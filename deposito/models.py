from django.db import models

class Deposito(models.Model):
    quantia = models.FloatField()
    destinatario_cpf = models.CharField(max_length=11)
    data_dep = models.DateField()
