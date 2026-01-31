from django.shortcuts import render, get_object_or_404, redirect
from .models import Activo
from .forms import ActivoForm


def home(request):
    activos = Activo.objects.all()
    return render(request, 'admin_it/home.html', {'activos': activos})


def activo_list(request):
    activos = Activo.objects.all()
    return render(request, 'admin_it/activo_list.html', {'activos': activos})


def activo_create(request):
    if request.method == 'POST':
        form = ActivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('it_admin:activo_list')
    else:
        form = ActivoForm()
    return render(request, 'admin_it/activo_form.html', {'form': form})


def activo_update(request, pk):
    activo = get_object_or_404(Activo, pk=pk)
    if request.method == 'POST':
        form = ActivoForm(request.POST, instance=activo)
        if form.is_valid():
            form.save()
            return redirect('it_admin:activo_list')
    else:
        form = ActivoForm(instance=activo)
    return render(request, 'admin_it/activo_form.html', {'form': form})


def activo_delete(request, pk):
    activo = get_object_or_404(Activo, pk=pk)
    if request.method == 'POST':
        activo.delete()
        return redirect('it_admin:activo_list')
    return render(request, 'admin_it/activo_confirm_delete.html', {'activo': activo})
