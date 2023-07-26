from django.contrib import admin
from .models import Post, UserPerfil, Comentario, ConexaoModel

admin.site.register(Post)
admin.site.register(UserPerfil)
admin.site.register(Comentario)
admin.site.register(ConexaoModel)
# Register your models here.
