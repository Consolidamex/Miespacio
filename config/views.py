from django.http import HttpResponse


def home(request):
    return HttpResponse("Carnalitos este pedo va funcionando")
