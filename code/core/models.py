from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
# Aqui nós a database.
# O Django vai criar uma pasta de imagens (profile) para nós

class Artista(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileing = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    nome = models.CharField(default="Ana", max_length=100)
    dataNasc = models.DateTimeField()
    email = models.EmailField(default="anabia@gmail.com", max_length=200)

    def __str__(self):
        return self.user.username
