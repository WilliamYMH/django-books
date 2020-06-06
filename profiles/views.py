from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordResetView, LoginView
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm
from django.urls import reverse_lazy


class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('index')
        self.object = None
        return super().get(request, *args, **kwargs)


class LoginUser(FormView):

    redirect_authenticated_user = True
    success_url = reverse_lazy('index')
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('index')
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request):
            return LoginView.as_view()(self.request)
        