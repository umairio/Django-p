import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from apprac.models import Profile, Project, Task

fake = Faker()

class Command(BaseCommand):
    help = 'Generates Fake Task'

    def handle(self, *args, **options):
        for _ in range(3):           
            p = random.choice(list(Project.objects.all()))
            task_member = [random.choice(list(p.team_member.all()))]          
            t = Task.objects.create(
                title = 'Task - ' + fake.word(),
                description = fake.text(),
                project = p,
            )
            t.assignee.set(task_member)
        self.stdout.write(self.style.SUCCESS('Fake Task generated.'))
