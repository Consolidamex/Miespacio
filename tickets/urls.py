# tickets/urls.py
from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='listar_tickets', permanent=False)),
    path('crear/', views.crear_ticket, name='crear_ticket'),
    path('listar/', views.listar_tickets, name='listar_tickets'),
]
