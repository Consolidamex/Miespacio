from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import TicketForm
from .models import Ticket

def crear_ticket(request):
    if not request.user.is_authenticated:
        return redirect('admin:login')
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tickets:listar_tickets')
    else:
        form = TicketForm()
    return render(request, 'tickets/crear_ticket.html', {'form': form})

def listar_tickets(request):
    tickets = Ticket.objects.all().order_by('-creado_en')
    
    # Búsqueda
    q = request.GET.get('q', '')
    if q:
        tickets = tickets.filter(Q(titulo__icontains=q) | Q(descripcion__icontains=q))
    
    # Filtro por estado
    estado = request.GET.get('estado', '')
    if estado:
        tickets = tickets.filter(estado=estado)
    
    # Paginación
    page_num = request.GET.get('page', 1)
    paginator = Paginator(tickets, 10)
    page = paginator.get_page(page_num)
    
    return render(request, 'tickets/listar_tickets.html', {
        'tickets': page.object_list,
        'paginator': paginator,
        'page': page,
        'q': q,
        'estado': estado,
    })

def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})

@login_required
def ticket_update(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('tickets:ticket_detail', pk=pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/ticket_form.html', {'form': form, 'ticket': ticket})

@login_required
def ticket_delete(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('tickets:listar_tickets')
    return render(request, 'tickets/ticket_confirm_delete.html', {'ticket': ticket})
