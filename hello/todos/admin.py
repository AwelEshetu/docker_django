from django.contrib import admin

# Register your models here.
from .models import Person, Todos, EmployeeInfo, LessID

#customize admin panel
class TodosAdmin(admin.ModelAdmin):
    list_display = ( "id" ,"task" , "day", "time", "get_person")
    def get_person(self, obj):
        return obj.person.user.username
    #Allows column order sorting
    get_person.admin_order_field  = 'firstname' 
    #Renames column head
    get_person.short_description = 'Person Name' 

admin.site.register(Person)
#register Todos with custom setting (above)
admin.site.register(Todos, TodosAdmin)
admin.site.register(EmployeeInfo)
admin.site.register(LessID)