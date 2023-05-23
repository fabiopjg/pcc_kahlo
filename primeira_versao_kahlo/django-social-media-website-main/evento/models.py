from django.db import models


class Evento(models.Model):
  tema = models.CharField(max_length=200)
  descricao = models.TextField()

# Create your models here.
