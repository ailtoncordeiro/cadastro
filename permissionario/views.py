from django.db import models
from django.shortcuts import render
#importação da classe TemplaView
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
#importar model
from .models import Permissionario

# Create your views here.

#Classe Página Inicial que herda a Classe TemplateView
class PaginaInicial(TemplateView):
    #Arquivo html que será renderizado
    template_name='index.html'

class PermissionarioListView(ListView):
    model = Permissionario
    template_name='permissionario-list.html'

class PermissionarioDetailView(DetailView):
    model = Permissionario
    template_name = 'permissionario-detail.html'

class PermissionarioCreateView(CreateView):
    model = Permissionario
    fields = ['nome','sobrenome','cpf']
    template_name = 'permissionario-create.html'
    success_url = reverse_lazy('permissionario-list')

class PermissionarioDeleteView(DeleteView):
    model = Permissionario
    template_name = 'permissionario-delete.html'
    success_url = reverse_lazy('permissionario-list')

class PermissionarioUpdateView(UpdateView):
    model = Permissionario
    fields = ['nome','sobrenome','cpf']
    template_name = 'permissionario-create.html'
    success_url = reverse_lazy('permissionario-list')