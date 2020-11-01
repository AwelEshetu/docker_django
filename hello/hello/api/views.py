from todos.models import Todos, EmployeeInfo
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import TodosSerializer, EmployeeInfoSerializer, UserSerializer

# EmployeInfo Viewset 

class EmployeeInfoViewSet(viewsets.ModelViewSet):
    queryset = EmployeeInfo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmployeeInfoSerializer

#Todos Viewset

class  TodosViewSet(viewsets.ModelViewSet):
    queryset = Todos.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodosSerializer

#User Viewset

class  UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer