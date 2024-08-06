from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import CreateView, TemplateView
from .forms import LoginUserForm, RegisterUserForm, UserPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    
    extra_context = {
        'title': 'Authorization'
    }


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')

    extra_context = {
        'title': 'registration'
    }


class MyProfile(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Profile of: {self.request.user.username}'
        return context
    

class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('password_change_done')

    extra_context = {
        'title': 'password change'
    }