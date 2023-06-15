from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import CustomUser, Group


# Create your views here.

class ProfileView(UpdateView):
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    model = CustomUser

    def get(self, request, *args, **kwargs):
        self.kwargs['pk'] = request.user.id
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.request.user.id,))


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.request.user.id,))


class RegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        print(Group.objects.first())
        context['groups'] = Group.objects.all()
        return context


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))
