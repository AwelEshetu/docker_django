from django.contrib import admin

# Register your models here.
from .models import Person, Todos, EmployeeInfo, LessID

#customize admin panel
class TodosAdmin(admin.ModelAdmin):
    list_display = ( "id" ,"task" , "day", "time")

admin.site.register(Person)
#register Todos with custom setting (above)
admin.site.register(Todos, TodosAdmin)
admin.site.register(EmployeeInfo)
admin.site.register(LessID)