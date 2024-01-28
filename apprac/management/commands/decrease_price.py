from django.core.management.base import BaseCommand
from apprac.models import Product
from django.db import models


class Command(BaseCommand):
    help = 'Decrease the price of all products by 10000'
    def handle(self, *args, **option):
        Product.objects.update(price=models.F('price') - 10000)
        self.stdout.write(self.style.SUCCESS('Prices decreased by 10k for all products.'))