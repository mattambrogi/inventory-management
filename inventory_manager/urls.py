from django.urls import path
from .views import (
  # Product Views
  ProductListView, 
  ProductCreateView, 
  ProductDetailView, 
  ProductUpdateView,
  ProductDeleteView,
  # Location Views
  LocationListView,
  LocationCreateView,
  LocationDeleteView,
  LocationUpdateView
)

urlpatterns = [
  # Location urls
  path("location/<int:pk>/edit/", LocationUpdateView.as_view(), name = "location_edit"),
  path("location/<int:pk>/delete/", LocationDeleteView.as_view(), name = "location_delete"),
  path("locations/new", LocationCreateView.as_view(), name = "location_create"),
  path("locations", LocationListView.as_view(), name = "location_list"),
  # Product urls
  path("product/new", ProductCreateView.as_view(), name = "product_create"),
  path("product/<int:pk>/", ProductDetailView.as_view(), name= "product_detail"),
  path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name= "product_edit"),
  path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name = "product_delete"),
  path("", ProductListView.as_view(), name="product_list"),
]