from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

class Evento(models.Model):
  tema = models.CharField(max_length=200)
  descricao = models.TextField()

class Postevento(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
  user = models.CharField(max_length=100)
  image = models.ImageField(upload_to='post_images')
  caption = models.TextField()
  created_at = models.DateTimeField(default=datetime.now)


  def __str__(self):
      return self.user



# Create your models here.
