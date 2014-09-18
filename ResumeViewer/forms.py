__author__ = 'Waz'
from django.contrib.auth.models import User
from ResumeViewer.models import UserProfile
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')