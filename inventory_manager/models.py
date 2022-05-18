from django.db import models
from django.urls import reverse

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length = 50, null = True, blank = True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
      return reverse("location_list")

class Product(models.Model):
    location = models.ForeignKey(Location, on_delete = models.CASCADE,null = True, blank = True )
    item_name = models.CharField(max_length = 50, null = True, blank = True)
    total_quantity = models.IntegerField(default = 0, null = True, blank = True)
    price = models.IntegerField(default = 0, null = True, blank = True)

    def __str__(self):
        return self.item_name
    def get_absolute_url(self):
      return reverse("product_list")