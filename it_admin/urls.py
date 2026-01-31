from django.urls import path
from . import views

app_name = 'it_admin'

urlpatterns = [
    path('', views.home, name='home_it'),
    path('activos/', views.activo_list, name='activo_list'),
    path('activos/crear/', views.activo_create, name='activo_create'),
    path('activos/<int:pk>/editar/', views.activo_update, name='activo_update'),
    path('activos/<int:pk>/eliminar/', views.activo_delete, name='activo_delete'),
]
