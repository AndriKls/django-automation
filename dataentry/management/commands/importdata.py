from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv

from dataentry.models import Student

class Command(BaseCommand):
    help = 'Imports data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the CSV file')
        parser.add_argument('model_name', type=str, help='The name of the model to import data into')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()
        
        model = None
        for app_config in apps.get_app_configs():
            try:
                mode = apps.get_model(app_config.label, model_name)
                break # break out of the loop if the model is found
            except LookupError:
                continue # continue to the next app_config if the model is not found
        if not model:
            raise CommandError(f'Model {model_name} not found')

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))