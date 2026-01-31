from django.http import HttpResponse

def home(request):
    return HttpResponse("Gestión de Tickets")
