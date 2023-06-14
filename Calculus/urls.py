from django.urls import path
from Calculus.views import IndexView, Task1View

app_name = 'Calculus'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task1', Task1View.as_view(), name='task1'),
]
