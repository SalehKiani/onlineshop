from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from.models import Product, Category, City, Address, Order, OrderItem, Review, CustomUser

admin.site.register(CustomUser, UserAdmin)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
