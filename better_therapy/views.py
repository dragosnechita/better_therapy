from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Client, Therapist, Appointment
from django.urls import reverse_lazy
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'
    title = 'Home'


class ClientView(TemplateView):
    template_name = 'client.html'
    title = 'Client'
    # badabeem


class ClientAddView(CreateView, PermissionRequiredMixin):
    model = Client
    template_name = 'client_add.html'
    fields = '__all__'
    success_url = reverse_lazy('client_list')
    permission_required = 'can_add_client'
    # badabeem


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'
    permission_required = 'can_view_client_list'
    # badabeem


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'
    context_object_name = 'clients'
    permission_required = 'can_view_client_details'
    # badabeem


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client_update.html'
    context_object_name = 'clients'
    fields = '__all__'
    success_url = reverse_lazy('clients_list')
    # badabeem


class ClientArchiveView(UpdateView):
    model = Client
    template_name = 'client_archive.html'  # badabeem
    context_object_name = 'clients'  # badabeem
    fields = '__all__'  # badabeem
    success_url = reverse_lazy('clients_list')  # badabeem
    # badabeem