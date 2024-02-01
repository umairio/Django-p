from django.core.management.base import BaseCommand
from apprac.models import User, Profile
from faker import Faker
import random

fake = Faker()
class Command(BaseCommand):
    help = 'Generates fake Users and Profile'
    def handle(self, *args, **option):
        for _ in range(5):
            u = User.objects.create(
                name = fake.name(),
                active = True
            )
            Profile.objects.create(
                user = u,
                role = random.choice([Profile.Role.Manager, Profile.Role.QA, Profile.Role.Developer]),
                phone_no = '+'+str(923000000000+round(random.uniform(100000000, 1000000000))),
            )    
        self.stdout.write(self.style.SUCCESS('Fake User Profile generated.'))
 