from django.core.management.base import BaseCommand
from dataentry.models import Student
import csv
class Command(BaseCommand):
    help = 'Imports data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Student.objects.create(roll_no=row['roll_no'], name=row['name'], age=row['age'])

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))