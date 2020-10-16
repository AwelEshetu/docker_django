from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Goodbye, world!")

def greet(request):
    return HttpResponse('Hello, Awel')
    
def goodbye(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")