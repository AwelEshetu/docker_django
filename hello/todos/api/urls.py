from django.conf.urls import url, include
from .views import TodosViewSet, EmployeeInfoViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employeeinfo', EmployeeInfoViewSet, basename='employeeinfo')
router.register('todos', TodosViewSet, basename='todos')
router.register('users', UserViewSet, basename='users')
urlpatterns = [
    url('', include(router.urls))
]