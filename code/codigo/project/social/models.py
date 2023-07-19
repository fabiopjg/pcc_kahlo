from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
    corpo = models.TextField()
    criado_em = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    image = models.ImageField(upload_to='uploads/post_images', blank=True, null=True)

class Comentario(models.Model):
    comentario = models.TextField()
    criado_em = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

class UserPerfil(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='perfil', on_delete=models.CASCADE)
    nome = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    aniversário=models.DateField(null=True, blank=True)
    localização = models.CharField(max_length=100, blank=True, null=True)
    foto = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png', blank=True)

    seguidores = models.ManyToManyField(User, blank=True, related_name='seguidores')


@receiver(post_save, sender=User)
def create_user_perfil(sender, instance, created, **kwargs):
	if created:
		UserPerfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_perfil(sender, instance, **kwargs):
	instance.perfil.save()

class ConexaoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

class MensagemModel(models.Model):
	conexao = models.ForeignKey('ConexaoModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
	sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	corpo = models.CharField(max_length=1000)
	data = models.DateTimeField(default=timezone.now)
	lido = models.BooleanField(default=False)

# Create your models here.
