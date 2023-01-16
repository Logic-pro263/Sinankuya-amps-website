from django import forms
from .models import Message, Post, Comments

"""
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
"""


class MessageForm(forms.ModelForm):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nom complet"}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Adresse email"}
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Votre message",
                "cols": "30",
                "rows": "7",
            }
        )
    )

    class Meta:
        model = Message
        fields = ["full_name", "email", "message"]


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "cols": "40", "rows": "5"}
        )
    )
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = Post
        fields = ["title", "content", "image"]
