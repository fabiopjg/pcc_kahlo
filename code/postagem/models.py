from django.db import models

class Postagem(models.Model):
    comentario = models.CharField(max_length=1000)
    legenda = models.CharField(max_length=1000)
    curtida = models.IntegerField()
    midia = models.IntegerField()
