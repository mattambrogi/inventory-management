from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Product, Location

class ProductListView(ListView):
  model = Product
  template_name = "product_list.html"

class ProductDetailView(DetailView):
  model = Product
  template_name = "product_detail.html"
  

class ProductCreateView(CreateView):
  model = Product
  template_name = "product_create.html"
  fields = ["item_name", "location", "price", "total_quantity"]

class ProductUpdateView(UpdateView):
  model = Product
  template_name = "product_edit.html"
  fields = ["item_name", "location", "price", "total_quantity"]

class ProductDeleteView(DeleteView):
  model = Product
  template_name = "product_delete.html"
  success_url = reverse_lazy("product_list")

class LocationListView(ListView):
  model = Location
  template_name = "location_manager.html"

class LocationCreateView(CreateView):
  model = Location
  template_name = "location_create.html"
  fields = ["name"]

class LocationDeleteView(DeleteView):
  model = Location
  template_name = "location_delete.html"
  success_url = reverse_lazy("location_list")

class LocationUpdateView(UpdateView):
  model = Location
  fields = ["name"]
  template_name = "location_edit.html"
  success_url = reverse_lazy("location_list")

  
