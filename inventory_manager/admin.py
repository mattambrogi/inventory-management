from django.contrib import admin

from .models import Product, Location, Stock

admin.site.register(Product)
admin.site.register(Location)
admin.site.register(Stock)

