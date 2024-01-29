from django.core.management.base import BaseCommand
from apprac.models import Customer
import random
from faker import Faker


fake=Faker()
class Command(BaseCommand):
    help = 'Generates fake data for the Customer models'
    
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Generating fake data...'))
        Customer.objects.create(
            name=fake.name(),
            phone_number=923000000000+round(random.uniform(100000000, 1000000000)),
        )
        self.stdout.write(self.style.SUCCESS('Fake customer data generation complete.'))
