from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Todos
# Create your views here.

#create form and validate it 
class TodosForm(forms.Form):
    task = forms.CharField(label="Task")
    day = forms.CharField(label="Day")
    time = forms.CharField(label="Time")

def index(request):
    #check if there is tasks in uses session and create empty list if there is not
    #"tasks":request.session["tasks"]
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, 'todos/index.html', {
        "tasks": Todos.objects.all()
    })

def add(request):
    #check if the form is has valid data and save it to tasks array, if not send back the add form 
    # if request is not post, initialize an empty form
    form = TodosForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            task = form.cleaned_data["task"]
            day  = form.cleaned_data["day"]
            time = form.cleaned_data["time"]
        
            task =  {
                "task": task,
                "day" : day,
                "time" : time
            }
            request.session["tasks"] += [task]
            #after adding a task redirect to the task list page
            return HttpResponseRedirect(reverse("todos:index"))
        else:
            return render(request, "todos/add.html",{
                "form": form
            })

    return render(request,'todos/add.html', {
        "form" : TodosForm()
    })

def task_detail( request, pk):
    #pk a must to have abaove
    task= Todos.objects.get(id=pk)
    return render( request, "todos/task_detail.html", {
        "task": task })