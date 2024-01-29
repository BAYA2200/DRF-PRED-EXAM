from django.contrib import admin

# Register your models here.
from shop.models import Category,Item,Order

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Order)
