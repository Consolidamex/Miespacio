from django.shortcuts import render
from .models import Activo


def home(request):
	activos = Activo.objects.all()
	return render(request, 'admin_it/home.html', {'activos': activos})
