from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'Calculus/index.html'


class Task1View(TemplateView):
    template_name = 'Calculus/task1.html'
