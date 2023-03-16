from django.db import models
from django.db.models.fields import CharField

class Cargos(models.Model):
    nome = CharField(max_length=50)

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    cargo = models.ManyToManyField(Cargos)

    def __str__(self):
        return self.nome
