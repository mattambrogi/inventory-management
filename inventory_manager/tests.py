from django.test import TestCase
from .models import Product, Location

class ProductTests(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.product = Product.objects.create(
      brand="Test Brand",
      item_name ="Hot Item",
      price=99.99,
    )
    
  def test_product_model(self):
    self.assertEqual(self.product.brand, "Test Brand")
    self.assertEqual(self.product.item_name, "Hot Item")
    self.assertEqual(self.product.price, 99.99)

class LocationTests(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.location = Location.objects.create(
      name="Warehouseville",
      zip_code ="12345",
    )
    
  def test_location_model(self):
    self.assertEqual(self.location.name, "Warehouseville")
    self.assertEqual(self.location.zip_code, "12345")
    