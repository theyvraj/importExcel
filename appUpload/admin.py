from django.contrib import admin
from .models import employee
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

class EmployeeResource(resources.ModelResource):
    is_active = Field(attribute='is_active', default=True)

    class Meta:
        model = employee
        import_id_fields = ['email']
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'department', 'salary', 'hire_date', 'is_active')

    def before_import_row(self, row, **kwargs):
        # Set default value for is_active if not present
        row['is_active'] = row.get('is_active', True)

@admin.register(employee)
class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource
    list_display = ['first_name', 'last_name', 'email', 'department', 'salary', 'hire_date', 'is_active', 'created_at', 'updated_at']
    search_fields = ['first_name', 'last_name', 'email', 'department']
    list_filter = ['department', 'is_active', 'hire_date', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['upload_button'] = format_html(
            '<a class="button" href="{}">Upload Excel File to Import Data</a>',
            'import/'
        )
        return super().changelist_view(request, extra_context=extra_context)