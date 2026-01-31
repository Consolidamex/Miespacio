from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticket

def crear_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tickets')
    else:
        form = TicketForm()
    return render(request, 'tickets/crear_ticket.html', {'form': form})

def listar_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/listar_tickets.html', {'tickets': tickets})
