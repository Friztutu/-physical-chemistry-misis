from django.contrib.auth.decorators import login_required
from django.urls import path
from users.views import ProfileView, UserLoginView, RegistrationView, logout

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', login_required(ProfileView.as_view()), name='profile'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', login_required(logout), name='logout'),
]

