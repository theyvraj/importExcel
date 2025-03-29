import pandas as pd
from django.core.management.base import BaseCommand
from appUpload.models import employee

class Command(BaseCommand):
    help = 'Import employees from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the Excel file to be imported')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            df = pd.read_excel(file_path)

            for _, row in df.iterrows():
                emp, created = employee.objects.update_or_create(
                    email=row['email'],
                    defaults={
                        'first_name': row['first_name'],
                        'last_name': row['last_name'],
                        'phone_number': row['phone_number'],
                        'department': row['department'],
                        'salary': row['salary'],
                        'hire_date': row['hire_date'],
                        'is_active': row['is_active']
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Added new employee: {emp}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated existing employee: {emp}'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing data: {e}'))