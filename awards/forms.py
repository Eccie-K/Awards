from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("profile_photo", "bio")

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length="200", help_text="required")
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ["poster"]

class VoteForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ("description",)
