import random

from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from apprac.models import Profile

fake = Faker()
class Command(BaseCommand):
    help = 'Generates fake Users and Profile'
    def handle(self, *args, **option):
        for _ in range(10):
            u = User.objects.create(
                username = fake.name(),
                password = 'admin'
            )
            Profile.objects.create(
                user = u,
                role = random.choice([Profile.Role.Manager, Profile.Role.QA, Profile.Role.Developer]),
                phone_no = '+' + str(9230 + random.randint(0, 4)) + str(random.randint(10000000, 100000000 )),
            )    
        self.stdout.write(self.style.SUCCESS('Fake User Profile generated.'))
 