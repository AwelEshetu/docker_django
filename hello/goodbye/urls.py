from django.urls import path
from . import views
#avoids namespace collusion for many apps index pages or so 
app_name = "goodbye"

urlpatterns=[
    path("", views.index, name="index"),
    path("<str:name>",views.goodbye, name="goodbye")

]