from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100, null=True, default="awel")
    lastname = models.CharField(max_length=100, null=True, default="eshetu")

    def __str__(self):
        return f"{self.firstname} : {self.lastname}"


class EmployeeInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    brief_exprience = models.TextField(max_length=500, null=True, blank=True)


class Todos(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    # relate Todos with Person table and delete todos related to persons when a person is deleted
    person = models.ForeignKey(
        EmployeeInfo, on_delete=models.CASCADE, related_name="persons"
    )

    def __str__(self):
        return f"You have '{self.task}' on '{self.day}' at '{self.time}' assigned to '{self.person}'."
        
    def calculate_product(self, x, y):
        return x*y

class LessID(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField(max_length=300, null=True, blank=True)
