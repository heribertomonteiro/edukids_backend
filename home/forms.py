from django import forms
from .models import Post, Evento

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'descricao', 'imagem']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descricao', 'data']