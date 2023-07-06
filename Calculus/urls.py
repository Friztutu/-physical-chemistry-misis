from django.urls import path
from Calculus.views import IndexView, Task1View, Result1View

app_name = 'Calculus'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task1/', Task1View.as_view(), name='task1'),
    path('result1/<int:task_id>/', Result1View.as_view(), name='result1'),
]
