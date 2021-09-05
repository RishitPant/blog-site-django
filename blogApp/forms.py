from django import forms
from django.forms import widgets
from .models import Post
from django.urls import reverse

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'author', 'post')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'post': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def get_absolute_url(self):
        return reverse('/')