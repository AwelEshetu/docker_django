from django.conf.urls import url, include
from .views import TodosViewSet, EmployeeInfoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/employeeinfo', EmployeeInfoViewSet, basename='employeeinfo')
router.register('api/todos', TodosViewSet, basename='todos')

urlpatterns = [
    url('', include(router.urls))
]