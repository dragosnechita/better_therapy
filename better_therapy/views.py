from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Client, Therapist, Supervisor
# Create your views here.


class HomeView(TemplateView):
    template_name = 'base.html'
    title = 'Home'