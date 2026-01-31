from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('listar/', views.listar_tickets, name='listar_tickets'),
    path('crear/', views.crear_ticket, name='crear_ticket'),
    path('<int:pk>/', views.ticket_detail, name='ticket_detail'),
    path('<int:pk>/editar/', views.ticket_update, name='ticket_update'),
    path('<int:pk>/eliminar/', views.ticket_delete, name='ticket_delete'),
]
