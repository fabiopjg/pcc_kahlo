from django import forms
from .models import Post, Comentario, ConexaoModel

class PostForm(forms.ModelForm):
    corpo = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Diga algo...'
            }))

    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['corpo', 'image']

class ComentarioForm(forms.ModelForm):
    comentario = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Diga algo...'
            }))
            
    class Meta:
        model = Comentario
        fields = ['comentario']

class ConexaoForm(forms.Form):
    username = forms.CharField(label='', max_length=100)

class MensagemForm(forms.Form):
    mensagem = forms.CharField(label='', max_length=1000)