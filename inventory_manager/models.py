from django.db import models
from django.urls import reverse


class Product(models.Model):
  brand = models.CharField(max_length = 50, null = True, blank = True)
  item_name = models.CharField(max_length = 50, null = True, blank = True)
  price = models.FloatField(default = 0, null = True, blank = True)

  def __str__(self):
      return self.item_name
    
  def get_absolute_url(self):
      return reverse("product_list")

class Location(models.Model):
  name = models.CharField(max_length = 50, null = True, blank = True)
  zip_code = models.CharField(max_length = 20, null = True, blank = True)

  def __str__(self):
      return self.name

class Stock(models.Model):
  product = models.ForeignKey(Product, on_delete = models.CASCADE,null = True, blank = True )
  location = models.ForeignKey(Location, on_delete = models.CASCADE,null = True, blank = True )
  quantity = models.IntegerField(default = 0, null = True, blank = True)

  class Meta:
    unique_together = ('product', 'location',)

  def __str__(self):
        return str(self.product) + ", " + str(self.location) 
  
