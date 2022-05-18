from django.contrib import admin

# Register your models here.
from .models import Location, Product

admin.site.register(Location)
admin.site.register(Product)