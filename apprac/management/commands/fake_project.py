# Standard Library Imports
import random
from datetime import date, timedelta

from django.core.management import call_command
from django.core.management.base import BaseCommand
from faker import Faker

from apprac.models import Profile, Project

fake = Faker()

class Command(BaseCommand):
    help = 'Generates fake Project'

    def handle(self, *args, **options):
        call_command('fake_user_profile')
        for _ in range(3):
            team_members = random.sample(list(Profile.objects.all()), k=3)
            print(team_members)
            p = Project.objects.create(
                title='Project - ' + fake.word(),
                description=fake.text(),
                end_date=date.today() + timedelta(days=random.randint(1, 30)),
            )
            p.team_member.set(team_members)
        call_command('fake_task')
        call_command('fake_doc')
        self.stdout.write(self.style.SUCCESS('Fake Projects and data generated.'))
