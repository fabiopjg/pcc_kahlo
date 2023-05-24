from django.urls import path

from . import views 

urlpatterns = [
    path('', views.listar, name='listar'),
    path('criar/', views.criar, name='criar'),
    path('excluir/<int:evento_id>', views.excluir, name='excluir'),
    path('editar/<int:evento_id>', views.editar, name="editar"),
    path('<int:evento_id>/', views.detail, name='detail'),
    path('upload', views.upload, name='upload'),
]

# Create your views here.


