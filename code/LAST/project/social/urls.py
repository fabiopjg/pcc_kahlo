from django.urls import path
from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, ComentarioDeleteView, PerfilView, PerfilEditView, AddSeguidor, RemoveSeguidor, AddLike, UserPesquisa, ListSeguidores, AddComentarioLike, CreateConexao, ListConexoes, ConexaoView, CreateMensagem

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comentario/delete/<int:pk>/', ComentarioDeleteView.as_view(), name='comentario-delete'),
    path('post/<int:post_pk>/comentario/<int:pk>/like', AddComentarioLike.as_view(), name='comentario-like'),

    path('post/<int:pk>/like', AddLike.as_view(), name='like'),

    path('perfil/<int:pk>/', PerfilView.as_view(), name='perfil'),
    path('perfil/edit/<int:pk>/', PerfilEditView.as_view(), name='perfil-edit'),

    path('perfil/<int:pk>/seguidores/add',AddSeguidor.as_view(), name='add-seguidor'),
    path('perfil/<int:pk>/seguidores/remove', RemoveSeguidor.as_view(), name='remove-seguidor'),
    path('perfil/<int:pk>/seguidores/', ListSeguidores.as_view(), name='list-seguidores'),

    path('pesquisa/', UserPesquisa.as_view(), name='perfil-pesquisa'),

    path('inbox/', ListConexoes.as_view(), name='inbox'),
    path('inbox/create-conexao', CreateConexao.as_view(), name='create-conexao'),
    path('inbox/<int:pk>/', ConexaoView.as_view(), name='conexao'),
    path('inbox/<int:pk>/create-mensagem/', CreateMensagem.as_view(), name='create-mensagem'),
]