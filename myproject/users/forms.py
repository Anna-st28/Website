from django import forms
from django.contrib.auth.models import User
from .models import PhotographerProfile, Photo


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class PhotographerProfileForm(forms.ModelForm):
    class Meta:
        model = PhotographerProfile
        fields = ['short_intro', 'bio', 'profile_image']


class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
