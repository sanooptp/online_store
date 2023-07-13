from django.urls import path
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html', authentication_form=LoginForm), name='login'),
    path('register/<int:pk>', views.RegistrationView.as_view(), name='register'),
    path('select/user/', views.UserselectView.as_view(), name='userselect'),
]