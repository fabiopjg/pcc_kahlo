from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import EventoForm
from .models import Evento

@login_required()
def listar(request):
    
    search = request.GET.get('search')

    if search:
        eventos = Evento.objects.filter(tema__icontains=search)
    else:
        eventos = Evento.objects.all()
    

    context = {
        'eventos': eventos
    }


    return render(request, 'eventos/listar.html', context)

@login_required()
def criar(request):

    if request.POST:
        form = EventoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/eventos')
    
    form = EventoForm()

    context = {
        'form': form,
    }

    return render(request, 'eventos/criar.html', context)

@login_required()
def excluir(request, evento_id):

    Evento.objects.get(pk=evento_id).delete()

    return HttpResponseRedirect("/eventos/") 

@login_required
def editar(request, evento_id):

    evento = Evento.objects.get(pk=evento_id)

    if request.POST:
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/eventos")
        
    else:
        form = EventoForm(instance=evento)

    context = {
        'form': form,
        'evento_id': evento_id
    }

    return render(request, 'eventos/editar.html', context)

@login_required
def detail(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    context = {
        'evento': evento
    }
    
    return render(request, 'eventos/detail.html', context)

@login_required(login_url='signin')
def upload(request):

    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

        return redirect('/')
    else:
        return redirect('/')
