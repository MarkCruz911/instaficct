"""Post forms."""
#Djando
from pyexpat import model
from django import forms

#Models
from posts.models import Post

class PostForm(forms.ModelForm):
    """Post model from."""

    class Meta:
        """Form settings."""
        model=Post
        fields = ('user', 'profile','title','photo')