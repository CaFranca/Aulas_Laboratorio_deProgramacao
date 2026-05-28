from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    quantidade = models.IntegerField(default=1)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
