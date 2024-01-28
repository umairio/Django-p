from django.contrib import admin
from .models import Customer, Product, Order
from django.db import models
import random
from faker import Faker


fake = Faker()

def generate_fake_data(modeladmin, request, queryset):
    for _ in range(5):  
        if issubclass(queryset.model, Product):
            Product.objects.create(
                name=fake.name(),
                company=fake.company(),
                price=round(random.uniform(10, 100000), 2),
            )
        elif issubclass(queryset.model, Customer):
            Customer.objects.create(
                name=fake.name(),
                phone_number=923000000000+round(random.uniform(100000000, 1000000000)),
            )

generate_fake_data.short_description = "Generate Fake Data"
admin.site.add_action(generate_fake_data)

def increase_price_by_10000(modeladmin, request, queryset):
    queryset.update(price=models.F('price') + 10000)

def decrease_price_by_10000(modeladmin, request, queryset):
    queryset.update(price=models.F('price') - 10000)

def order_completed(modeladmin, request, queryset):
    queryset.update(status='completed')

def order_pending(modeladmin, request, queryset):
    queryset.update(status='pending')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "phone_number"]
    list_filter = ["phone_number"]
    search_fields = ["name",'phone_number']
    ordering = ['name']
    actions = [generate_fake_data]

class ProductAdmin(admin.ModelAdmin):
    change_form_template = "admin/management/custom_change_form.html"
    
    def response_change(self, request, obj):
        if "_price_hike_10k" in request.POST:
            obj.price += 10000
            obj.save()
            self.message_user(request, "Price increased by 10k.")
            return super().response_change(request, obj)

        if "_price_reduce_10k" in request.POST:
            obj.price -= 10000
            obj.save()
            self.message_user(request, "Price decreased by 10k.")
            return super().response_change(request, obj)

        return super().response_change(request, obj)

    list_display = ["name",'company', "price"]
    list_filter = ["company",'price']
    search_fields = ["name",'company','price']
    ordering = ['name','price']
    actions = [increase_price_by_10000, decrease_price_by_10000, generate_fake_data]
    
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'get_products', 'status']
    list_filter = ['id', 'customer', 'status']
    search_fields = ['id', 'customer', 'status']
    ordering = ['status']
    actions = [order_completed,order_pending]


    def get_products(self, obj):
        return ", ".join([str(product) for product in obj.products.all()])

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)