from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Prints a greeting to the console'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='The name to greet')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greeting = f'Hail {name}!'
        self.stdout.write(self.style.SUCCESS(greeting))