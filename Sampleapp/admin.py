from django.contrib import admin
# Register your models here.
from Sampleapp .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    class Meta:
        model = Employee
        fields ='__all__'

admin.site.register(Employee,EmployeeAdmin)
