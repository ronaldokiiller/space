from django.db import models
from django.contrib.auth.models import User


class Imagem(models.Model):



    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='galeria/')
    descricao = models.TextField(blank=True)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo