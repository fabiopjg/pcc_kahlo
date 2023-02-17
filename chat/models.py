from django.db import models

class Chat(models.Model):
    data = models.DateTimeField()
    horario = models.IntegerField(default=0)
    visualizacao = models.IntegerField(default=0)
