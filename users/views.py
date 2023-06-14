from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.

class ProfileView(TemplateView):
    template_name = 'users/profile.html'


class LoginView(TemplateView):
    template_name = 'users/login.html'


class RegistrationView(TemplateView):
    template_name = 'users/registration.html'
