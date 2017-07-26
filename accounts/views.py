from django.views.generic import (
    FormView,
    CreateView,
    RedirectView,
)

from django.contrib.auth import (
    login,
    logout,
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from .models import User
from .forms import (
    LoginForm,
    RegisterForm,
)

class LoginView(FormView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('core:index')
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('core:index'))
        return super(LoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

class LogoutView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('core:index')
    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    model = User
    success_url = reverse_lazy('core:index')
    form_class = RegisterForm
