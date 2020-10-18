from django.contrib import admin

# Register your models here.
from .models import Person, Todos

admin.site.register(Person)
admin.site.register(Todos)
