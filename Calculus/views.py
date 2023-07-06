from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from Calculus.forms import Task1Form
from Calculus.models import Task1, ResultTask1


# Create your views here.

class IndexView(TemplateView):
    template_name = 'Calculus/index.html'


class Task1View(CreateView):
    template_name = 'Calculus/task1.html'
    model = Task1
    form_class = Task1Form

    def get_success_url(self):
        last = Task1.objects.last()
        if not last:
            return reverse_lazy('main:result1', args=(1,))
        else:
            return reverse_lazy('main:result1', args=(last.id,))


class Result1View(TemplateView):
    template_name = 'Calculus/result1.html'

    def get_context_data(self, **kwargs):
        context = super(Result1View, self).get_context_data(**kwargs)
        context['result1'] = ResultTask1.objects.get(task_id=self.kwargs.get('task_id'))
        return context
