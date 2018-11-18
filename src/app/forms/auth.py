from django.contrib.auth import forms
from app.models import User


class RegisterForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)
