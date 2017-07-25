from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)

class LoginForm(AuthenticationForm):
    pass

class RegisterForm(UserCreationForm):
    pass
