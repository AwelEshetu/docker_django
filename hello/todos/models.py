from django.db import models

# Create your models here.
import uuid
from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=100, null=True , default="awel")
    lastname = models.CharField(max_length=100, null=True , default="eshetu")

    def __str__(self):
        return f"{self.firstname} : {self.lastname}"

class Todos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
#relate Todos with Person table and delete todos related to persons when a person is deleted
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="persons")

    def __str__(self):
        return f"You have '{self.task}' on '{self.day}' at '{self.time}' assigned to '{self.person}'."