from django.contrib import admin
from .models import employee

@admin.register(employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'department', 'salary', 'hire_date', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')