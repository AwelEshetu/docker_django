from django.urls import path
from . import views
#avoids namespace collusion for many apps
app_name = "todos"

urlpatterns=[
    path("",views.index , name="index"),
    path("add", views.add, name="add")
]