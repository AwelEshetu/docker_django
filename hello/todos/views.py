from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Todos, Person, EmployeeInfo
from django.views.generic import DetailView, ListView
# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile

# create form and validate it
class TodosForm(forms.Form):
    task = forms.CharField(label="Task")
    day = forms.CharField(label="Day")
    time = forms.CharField(label="Time")

class TodosListView(ListView):
    model = Todos
    template_name = 'todos/index.html'
    context_object_name = 'tasks'
    
    def get_context_data(self, *kwargs):
        context = super().get_context_data(*kwargs)
        emplyees = EmployeeInfo.objects.all()
        context['employees'] = emplyees
        return context

    def calculate_sum(self, x, y):
        return x+y
    
def add(request):
    # check if the form is has valid data and save it to tasks array, if not send back the add form
    # if request is not post, initialize an empty form
    form = TodosForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            task = form.cleaned_data["task"]
            day = form.cleaned_data["day"]
            time = form.cleaned_data["time"]
            p = Person()
            p.save()
            t = Todos(task=task, day=day, time=time, person=p)
            t.save()
            # after adding a task redirect to the task list page
            return HttpResponseRedirect(reverse("todos:index"))
        else:
            return render(request, "todos/add.html", {"form": form})

    return render(request, "todos/add.html", {"form": TodosForm()})


def task_detail(request, id):
    # pk a must to have abaove
    # task.persons.all() -> will get all persons related to the task ( persons <- mentioned as related name in the models)
    task = Todos.objects.get(id=id)

    return render(
        request,
        "todos/task_detail.html",
        {
            "task": task,
        },
    )


def cv_to_pdf(request):
    """Generate pdf."""
    # Model data
    print(f'the request object coming is {request}')
    
    task = {"task": "hello", "day": "monday", "time": "wholeday"}

    # Rendered
    html_string = render_to_string("todos/task_detail.html", {"task": task})
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type="application/pdf;")
    response["Content-Disposition"] = "inline; filename=list_people.pdf"
    response["Content-Transfer-Encoding"] = "binary"
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, "rb")
        response.write(output.read())

    return response