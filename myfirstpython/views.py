from django.http import HttpResponse

def home(request):
    return HttpResponse("Boilerplate Django App")