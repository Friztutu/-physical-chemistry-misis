from django.urls import path
from users.views import ProfileView, LoginView, RegistrationView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]

