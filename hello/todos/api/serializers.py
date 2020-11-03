from rest_framework import serializers
from todos.models import Todos, EmployeeInfo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EmployeeInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = EmployeeInfo
        fields = '__all__'
        

class TodosSerializer(serializers.ModelSerializer):
    person = EmployeeInfoSerializer()
    class Meta:
        model = Todos
        fields = '__all__'

    def create(self, validated_data):
        
        person_data = validated_data.pop('person')
        user_data = person_data.pop('user')
        user= User.objects.create(**user_data)
        person = EmployeeInfo.objects.create(user=user, **person_data)
        todos = Todos.objects.create(**validated_data, person=person)
        return todos
        

