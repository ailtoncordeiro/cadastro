from django.urls import path
#Importar as view
from .views import *


urlpatterns = [

    path('',PaginaInicial.as_view(), name='index'),
    path('permissionario/list', PermissionarioListView.as_view(), name='permissionario-list'),
    path('permissionario/detail/<int:pk>', PermissionarioDetailView.as_view(), name='permissionario-detail'),
    path('permissionario/create', PermissionarioCreateView.as_view(), name='permissionario-create'),
    path('permissionario/delete/<int:pk>', PermissionarioDeleteView.as_view(), name='permissionario-delete'),
    path('permissionario/update/<int:pk>', PermissionarioUpdateView.as_view(), name='permissionario-update'),

]


