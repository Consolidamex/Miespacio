from django.urls import path
from . import views

app_name = 'it_admin'

urlpatterns = [
    path('', views.home, name='home_it'),
]
