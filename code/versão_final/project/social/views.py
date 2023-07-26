from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post, Comentario, UserPerfil, ConexaoModel, MensagemModel

from .forms import PostForm, ComentarioForm, ConexaoForm, MensagemForm

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Q

from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

class PostListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logged_in_user = request.user
        posts = Post.objects.filter(
            autor__perfil__seguidores__in=[logged_in_user.id]
        ).order_by('-criado_em')
        form = PostForm()

        context = {
            'post_list' : posts,
            'form' : form,
        }

        return render(request, 'social/post_list.html', context)

    def post(self, request, *args, **kwargs):
        logged_in_user = request.user
        posts = Post.objects.filter(
            autor__perfil__seguidores__in=[logged_in_user.id]
        ).order_by('-criado_em')
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.autor = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'social/post_list.html', context)

class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = ComentarioForm()

        comentarios = Comentario.objects.filter(post=post).order_by('-criado_em')

        context = {
            'post' : post,
            'form' : form,
            'comentarios' : comentarios,
        }

        return render(request, 'social/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = ComentarioForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.autor = request.user
            new_comment.post = post
            new_comment.save()

        comentarios = Comentario.objects.filter(post=post).order_by('-criado_em')

        context = {
            'post' : post,
            'form' : form,
            'comentarios' : comentarios,
        }

        return render(request, 'social/post_detail.html', context)

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['corpo']
    template_name = 'social/post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'social/post_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor

class ComentarioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comentario
    template_name = 'social/comentario_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor

class PerfilView(View):
    def get(self, request, pk, *args, **kwargs):
        perfil = UserPerfil.objects.get(pk=pk)
        user = perfil.user
        posts = Post.objects.filter(autor=user).order_by('-criado_em')

        seguidores = perfil.seguidores.all()

        if len(seguidores) == 0:
            is_seguindo = False

        for seguidor in seguidores:
            if seguidor == request.user:
                is_seguindo = True
            else:
                is_seguindo = False


        numero_seguidores = len(seguidores)

        context = {
            'user' : user,
            'perfil' : perfil,
            'posts' : posts,
            'numero_seguidores' : numero_seguidores,
            'is_seguindo' : is_seguindo,
        }
    
        return render(request, 'social/perfil.html', context)

class PerfilEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserPerfil
    fields = ['nome', 'bio', 'aniversário', 'localização', 'foto']
    template_name = 'social/perfil_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('perfil', kwargs={'pk': pk})

    def test_func(self):
        perfil = self.get_object()
        return self.request.user == perfil.user

class AddSeguidor(LoginRequiredMixin, View):
    
    def post(self, request, pk, *args, **kwargs):
        perfil = UserPerfil.objects.get(pk=pk)
        perfil.seguidores.add(request.user)

        return redirect('perfil', pk=perfil.pk)

class RemoveSeguidor(LoginRequiredMixin, View):
    
    def post(self, request, pk, *args, **kwargs):
        perfil = UserPerfil.objects.get(pk=pk)
        perfil.seguidores.remove(request.user)

        return redirect('perfil', pk=perfil.pk)

class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)
            
        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class UserPesquisa(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        perfil_list = UserPerfil.objects.filter(
            Q(user__username__icontains=query)
        )

        context = {
            'perfil_list': perfil_list,
        }

        return render(request, 'social/pesquisa.html', context)

class ListSeguidores(View):
    def get(self, request, pk, *args, **kwargs):
        perfil = UserPerfil.objects.get(pk=pk)
        seguidores = perfil.seguidores.all()

        context = {
            'perfil': perfil,
            'seguidores': seguidores,
        }

        return render(request, 'social/seguidores_list.html', context)


class ListConexoes(View):
    def get(self, request, *args, **kwargs):
        conexoes = ConexaoModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))

        context = {
            'conexoes': conexoes
        }

        return render(request, 'social/inbox.html', context)

class CreateConexao(View):
    def get(self, request, *args, **kwargs):
        form = ConexaoForm()

        context = {
            'form': form
        }

        return render(request, 'social/create_conexao.html', context)

    def post(self, request, *args, **kwargs):
        form = ConexaoForm(request.POST)

        username = request.POST.get('username')

        try:
            receiver = User.objects.get(username=username)
            if ConexaoModel.objects.filter(user=request.user, receiver=receiver).exists():
                conexao = ConexaoModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('conexao', pk=conexao.pk)
            elif ConexaoModel.objects.filter(user=receiver, receiver=request.user).exists():
                conexao = ConexaoModel.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect('conexao', pk=conexao.pk)

            if form.is_valid():
                conexao = ConexaoModel(
                    user=request.user,
                    receiver=receiver
                )
                conexao.save()

                return redirect('conexao', pk=conexao.pk)
        except:
            messages.error(request, 'Invalid username')
            return redirect('create-conexao')

class ConexaoView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MensagemForm()
        conexao = ConexaoModel.objects.get(pk=pk)
        mensagem_list = MensagemModel.objects.filter(conexao__pk__contains=pk)
        context = {
            'conexao': conexao,
            'form': form,
            'mensagem_list': mensagem_list
        }

        return render(request, 'social/conexao.html', context)

class CreateMensagem(View):
    def post(self, request, pk, *args, **kwargs):
        conexao = ConexaoModel.objects.get(pk=pk)
        if conexao.receiver == request.user:
            receiver = conexao.user
        else:
            receiver = conexao.receiver

        mensagem = MensagemModel(
            conexao=conexao,
            sender_user=request.user,
            receiver_user=receiver,
            corpo=request.POST.get('mensagem')
        )

        mensagem.save()
        return redirect('conexao', pk=pk)

