from django.core.management.base import BaseCommand
from apprac.models import Profile, Project
from django.contrib.auth.models import User
from faker import Faker
import random
from datetime import date, timedelta


fake = Faker()

class Command(BaseCommand):
    help = 'Generates fake Project'

    def handle(self, *args, **options):
        for _ in range(3):
            team_members = random.sample(list(Profile.objects.all()), k=3)
            print(team_members)
            p = Project.objects.create(
                title='Project - ' + fake.word(),
                description=fake.text(),
                end_date=date.today() + timedelta(days=random.randint(1, 30)),
            )
            p.team_member.set(team_members)
        self.stdout.write(self.style.SUCCESS('Fake Projects generated.'))
