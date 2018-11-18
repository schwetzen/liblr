from django.views import generic
from django.contrib.auth import views
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from app.forms import RegisterForm


class LoginView(views.LoginView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseForbidden('Forbidden')
        return super().post(request, *args, **kwargs)


class LogoutView(views.LogoutView):
    ...


class RegisterView(generic.CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
