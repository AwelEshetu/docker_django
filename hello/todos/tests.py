from django.test import TestCase
from .views import TodosListView
from .models import Todos, EmployeeInfo
from django.contrib.auth.models import User

# Create your tests here.
class TodoListViewTest(TestCase):
    def setUp(self):
        self.view = TodosListView()

    def test_attrs(self):
        self.assertEqual(self.view.model, Todos)
        self.assertEqual(self.view.context_object_name, 'tasks')
        self.assertEqual(self.view.template_name, 'todos/index.html')

    def test_calculate_sum(self):
        self.assertEqual(self.view.calculate_sum(4,5), 9)

class TodosModelTest(TestCase):
   
    def setUp(self):
        user = User.objects.create(username='awel',email='awel@awel.com')
        self.employee = EmployeeInfo.objects.create(
            user = user,
            title = 'runner',
            brief_exprience='not available yet'
            )
        self.todos = Todos.objects.create(
            task = 'Clean your room',
            day = 'Thursday',
            time = 'Whole day',
            person = self.employee
        )
   
    def test_fields(self):
      
        self.assertEqual(self.employee.user.username, 'awel')
        self.assertEqual(self.todos.person.user.username, 'awel')
        self.assertEqual(self.todos.task,'Clean your room')
        self.assertEqual(self.todos.time, 'Whole day')
   
    def test_calculate_product(self):
        self.assertEqual(self.todos.calculate_product(4,5),20)
    