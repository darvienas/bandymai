from django.contrib import admin
from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'position')
    list_filter = ('f_name', 'l_name', 'position')
    search_fields = ('f_name', 'l_name', 'position')

class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name',)


# Register your models here.
admin.site.register(Client)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Task)
admin.site.register(Bill)
admin.site.register(Project, ProjectAdmin)