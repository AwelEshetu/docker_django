from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "goodbye/index.html")

def goodbye(request , name):
    return render(request, "goodbye/goodbye.html", {
        "name":name.capitalize()
    })
