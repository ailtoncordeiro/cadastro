from django.shortcuts import render
#importação da classe TemplaView
from django.views.generic import TemplateView

# Create your views here.

#Classe Página Inicial que herda a Classe TemplateView
class PaginaInicial(TemplateView):
    #Arquivo html que será renderizado
    template_name='index.html'


