from django.urls import path
#Importar as view
from .views import *


urlpatterns = [

    path('',PaginaInicial.as_view(), name='index'),
    path('permissionario/list', PermissionarioListView.as_view(), name='permissionario-list'),

]


