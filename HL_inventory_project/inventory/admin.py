from django.contrib import admin
from .models import Factory, Product, Material, Item

admin.site.register(Factory)
admin.site.register(Product)
admin.site.register(Material)
admin.site.register(Item)