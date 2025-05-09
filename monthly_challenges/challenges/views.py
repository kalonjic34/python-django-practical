from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def jan(request):
    return HttpResponse("Eat no meat for the entire month!")

def feb(request):
    return HttpResponse("walk for at least 20 minutes every day!")