from django.urls import path
from . import views

# avoids namespace collusion for many apps
app_name = "todos"

urlpatterns = [
    path("", views.TodosListView.as_view(), name="index"),
    path("add", views.add, name="add"),
    path("<id>/", views.task_detail, name="detail"),
    path("pdf", views.cv_to_pdf, name="to_pdf"),
]
