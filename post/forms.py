from django import forms
from .models import Post
from django.contrib.auth.models import User

class PostForms(forms.ModelForm):
    class Meta:
        model=Post
        fields=["title","content","image"]

class create_userForm(forms.ModelForm):
    class Meta:
        model = User
        fields=["username","first_name"]