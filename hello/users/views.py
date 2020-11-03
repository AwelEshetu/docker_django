from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django import  forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-group'}))

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "todos/index.html")
'''
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("todos:index"), {
                "user": request.user.first_name
            })
        else:
            return render(request, "users/login.html", {
                "message" : "Invalid credentials."
            })
    return render(request, "users/login.html")
'''
def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return HttpResponseRedirect(reverse("todos:index"), {
                "user": request.user.first_name
            })
        else:
            return render(request, "users/login.html", {
                 "form" : form
            })
    return render(request, "users/login.html",{
                 "form" : LoginForm
            })
def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message" : "Logged out.",
        "form" : LoginForm
    })