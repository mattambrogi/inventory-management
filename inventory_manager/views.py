from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product, Location, Stock


class HomeView(TemplateView):
    template_name = "home.html"

'''
Product Views: List, Create, Update, Delete
'''

class ProductListView(ListView):
  model = Product
  template_name = "product_templates/product_list.html"

class ProductCreateView(CreateView):
  model = Product
  template_name = "product_templates/product_create.html"
  fields = ["brand", "item_name", "price"]
  
class ProductUpdateView(UpdateView):
  model = Product
  template_name = "product_templates/product_edit.html"
  fields = ["brand", "item_name", "price"]

class ProductDeleteView(DeleteView):
  model = Product
  template_name = "product_templates/product_delete.html"
  success_url = reverse_lazy("product_list")

'''
Location Views: List, Create, Update, Delete
'''

class LocationListView(ListView):
  model = Location
  template_name = "location_templates/location_list.html"
  
class LocationCreateView(CreateView):
  model = Location
  template_name = "location_templates/location_create.html"
  fields = ["name", "zip_code"]
  success_url = reverse_lazy("location_list")
  
class LocationUpdateView(UpdateView):
  model = Location
  fields = ["name", "zip_code"]
  template_name = "location_templates/location_edit.html"
  success_url = reverse_lazy("location_list")

class LocationDeleteView(DeleteView):
  model = Location
  template_name = "location_templates/location_delete.html"
  success_url = reverse_lazy("location_list")

'''
Core Stock Views: List, Create, Update, Delete
'''

class StockListView(ListView):
  model = Stock
  template_name = "stock_templates/stock_list.html"
  ordering = ['product']

class StockCreateView(CreateView):
  model = Stock
  template_name = "stock_templates/stock_create.html"
  fields = ["product", "location", "quantity"]
  success_url = reverse_lazy("stock_list")

class StockUpdateView(UpdateView):
  model = Stock
  template_name = "stock_templates/stock_edit.html"
  fields = ["product", "location", "quantity"]
  success_url = reverse_lazy("stock_list")

class StockDeleteView(DeleteView):
  model = Stock
  template_name = "stock_templates/stock_delete.html"
  success_url = reverse_lazy("stock_list")

'''
Extra Stock Views: 
- See all stock at a given location
- See all stock for a given product across locations
'''

class StockLocationListView(ListView):
  template_name = "stock_list.html"
  def get_queryset(self):
        self.location = get_object_or_404(Location, zip_code=self.kwargs['zip_code'])
        return Stock.objects.filter(location=self.location).order_by('product')

class StockProductListView(ListView):
  template_name = "stock_list.html"
  def get_queryset(self):
        self.product = get_object_or_404(Product, pk=self.kwargs['id'])
        return Stock.objects.filter(product=self.product).order_by('location')
  