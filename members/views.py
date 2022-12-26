from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class UserRegistrationView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')



class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "registration/registration.html" 