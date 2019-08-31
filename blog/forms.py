from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        # author should be the person who is currently logged in 
        # created_date should be automatically set when we create a post