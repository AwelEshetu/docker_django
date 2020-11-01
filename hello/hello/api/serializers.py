from rest_framework import serializers
from todos.models import Todos, EmployeeInfo
from django.contrib.auth.models import User

class EmployeeInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeInfo
        fields = '__all__'

class TodosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todos
        fields = '__all__'
        depth = 1