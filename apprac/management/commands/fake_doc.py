import random
from io import BytesIO

from django.contrib.auth.models import User
from django.core.files import File
from django.core.management.base import BaseCommand
from faker import Faker

from apprac.models import Document, Project

fake = Faker()

class Command(BaseCommand):
    help = 'Generates fake Documents for Task Management'

    def handle(self, *args, **options):
        p = random.choice(list(Project.objects.all()))
        Document.objects.create(
            name='Doc ' + fake.word(),
            description=fake.text(),
            version=f"v{fake.random_int(2024, 2030)}.{fake.random_int(1, 12)}.{fake.random_int(1, 30)}{fake.random_letter().lower()}",
            project = p,
        )
