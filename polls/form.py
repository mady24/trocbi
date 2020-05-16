from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class UserForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'username')
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address', 'tel')
class AvatarForm(forms.ModelForm):
    avatar = forms.ImageField()
    class Meta:
        model = Avatar
        fields = ['avatar']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['mail']