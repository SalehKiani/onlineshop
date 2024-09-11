from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from.models import Product, Category, City, Address, Order, OrderItem, Review, User

admin.site.register(User, UserAdmin)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
