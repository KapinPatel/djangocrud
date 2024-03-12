from django.contrib import admin
from crudApp.models import Company, Employee
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location')
    search_fields=('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','phone','company')
    list_filter=('company',)

admin.site.register(Company, CompanyAdmin )
admin.site.register(Employee,EmployeeAdmin)