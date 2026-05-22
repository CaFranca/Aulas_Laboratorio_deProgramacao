from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=50, unique=True)
    curso = models.CharField(max_length=150)
    idade = models.PositiveIntegerField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
