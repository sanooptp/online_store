from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from .forms import RegistrationForm
from django.shortcuts import redirect


class CustomLoginView(LoginView):
    success_url = 'home' 


class RegistrationView(FormView):
    template_name = 'users/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')  # Replace 'home' with the URL name of your home page

    def form_valid(self, form):
        if self.kwargs.get("pk"):
            form.instance.is_seller = True
        form.save()
        return super().form_valid(form)


class UserselectView(TemplateView):
    template_name = 'users/userselect.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('admin'))
        else: 
             return redirect(reverse_lazy('userselect'))