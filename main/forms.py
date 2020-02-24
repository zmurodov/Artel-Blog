from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}),
                           max_length=50, help_text='Name')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
                             max_length=254, help_text='Email')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               max_length=50, help_text='Password')
