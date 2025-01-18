# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Replace CustomUser with your custom user model if you have one
        fields = ['username', 'email','password']  # Add more fields if needed

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
