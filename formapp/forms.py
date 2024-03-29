from django import forms
from .models import PostModel

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('image','title', 'author', 'first_name', 'last_name')