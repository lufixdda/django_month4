from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from . import models, forms


class RegisterView(CreateView):
    form_class = forms.CustomRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class AuthLoginView(LoginView):
    authentication_form = forms.LoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('profile')


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = models.CustomUser.objects.get(id=self.request.user.id)
        return context
