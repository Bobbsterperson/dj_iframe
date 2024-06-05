from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import MyApp

def index(request):
    return render(request, 'myapp/index.html')