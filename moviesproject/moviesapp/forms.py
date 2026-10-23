from django import forms

from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'image_url']
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'image_url': 'URL do pôster',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://'}),
        }