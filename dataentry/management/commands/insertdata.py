from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = 'Inserts data into the database'

    def handle(self, *args, **kwargs):
        for data in dataset:

            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()

            if not existing_record:
                Student.objects.create(roll_no=roll_no, name=name, age=age)
            else:
                self.stdout.write(self.style.WARNING(f'Record with roll number {roll_no} already exists'))
                
            self.stdout.write(self.style.SUCCESS('Data inserted successfully'))
