from django.db import models

class Evento(models.Model):
    data = models.DateTimeField()
    local = models.CharField(max_length=100)
    nomeEvento = models.CharField(max_length=100)
    biografiaEvento = models.CharField(max_length=500)
    fotoCapaEvento = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
