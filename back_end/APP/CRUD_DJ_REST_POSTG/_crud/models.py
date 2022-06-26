from django.db import models

# Create your models here.
class Atividade(models.Model):
    Sede = models.CharField(max_length=500)
    Lotaçao = models.CharField(max_length=500)
    cargo = models.CharField(max_length=500)

class Funcionario(models.Model):
    matricula = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=500)
    setor = models.CharField(max_length=500)
    ativo = models.BooleanField(default=False)
    foto = models.CharField(max_length=500)

class Situação(models.Model):
    operacional = models.BooleanField(primary_key=True,default=False)
    motivo = models.TextField()