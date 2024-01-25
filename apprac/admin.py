from django.contrib import admin
from .models import Customer, Product, Order
from django.db import models

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

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name",'company', "price"]
    list_filter = ["company",'price']
    search_fields = ["name",'company','price']
    ordering = ['name','price']
    actions = [increase_price_by_10000,decrease_price_by_10000]
    
    
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