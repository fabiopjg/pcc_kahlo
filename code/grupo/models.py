from django.db import models

class Grupo(models.Model):
    nomeGrupo = models.CharField(max_length=100)
    biografiaGrupo = models.CharField(max_length=500)
    fotoCapaGrupo = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
