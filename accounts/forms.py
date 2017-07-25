from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)

from .models import User

class LoginForm(AuthenticationForm):
    pass

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',]
