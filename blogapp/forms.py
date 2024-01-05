from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User,Blog

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']


class BlogForm(forms.ModelForm):
    class Meta: 
        model=Blog
        fields = ['title','content']       



class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)      

