from django.forms import ModelForm

from .models import Evento

class EventoForm(ModelForm):
  class Meta:
    model = Evento
    fields = '__all__'


