from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'dashboard/dashboard.html')

def listaPacientes(request):
    return render(request, 'dashboard/listaPacientes.html')