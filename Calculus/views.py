from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from Calculus.forms import Task1Form
from Calculus.models import Task1


# Create your views here.

class IndexView(TemplateView):
    template_name = 'Calculus/index.html'


class Task1View(CreateView):
    template_name = 'Calculus/task1.html'
    model = Task1
    success_url = reverse_lazy('main:result1')
    form_class = Task1Form

