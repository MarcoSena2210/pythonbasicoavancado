'''
   Sempre que houver alteração nno banco/tabela usar:
    py manage.py makemigrations
    py manage.py migrate
'''

from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=60)
    sobrenome = models.CharField(max_length=60, blank=True)
    telefone = models.CharField(max_length=150)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now )
    descricao = models.TextField(blank=True)
    ## Relacionamento
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y%m/')


    def __str__(self):
        return self.nome
