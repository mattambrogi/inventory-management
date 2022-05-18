from django.urls import path
from .views import (
  HomeView,
  # Product Views
  ProductListView,
  ProductCreateView,
  ProductDeleteView,
  ProductUpdateView,
  # Location Views
  LocationListView,
  LocationCreateView,
  LocationDeleteView,
  LocationUpdateView,
  # Stock Views
  StockListView,
  StockCreateView,
  StockUpdateView,
  StockDeleteView,
  StockLocationListView,
  StockProductListView,
)

urlpatterns = [
  # Stock urls
  path("stock/<int:pk>/delete/", StockDeleteView.as_view(), name = "stock_delete"),
  path("stock/<int:pk>/edit/", StockUpdateView.as_view(), name= "stock_edit"),
  path("stock/new/", StockCreateView.as_view(), name="stock_create"),
  path("stock/product/<id>/", StockProductListView.as_view(), name="stock_product_list"),
  path("stock/location/<zip_code>/", StockLocationListView.as_view(), name="stock_location_list"),
  path("stock/", StockListView.as_view(), name="stock_list"),

  # Location urls
  path("locations/<int:pk>/delete/", LocationDeleteView.as_view(), name = "location_delete"),
  path("locations/<int:pk>/edit/", LocationUpdateView.as_view(), name = "location_edit"),
  path("locations/new/", LocationCreateView.as_view(), name="location_create"),
  path("locations/", LocationListView.as_view(), name="location_list"),

  # Product urls
  path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name = "product_delete"),
  path("products/<int:pk>/edit/", ProductUpdateView.as_view(), name= "product_edit"),
  path("products/new/", ProductCreateView.as_view(), name="product_create"),
  path("products/", ProductListView.as_view(), name="product_list"),
  # Home
  path("", HomeView.as_view(), name="home"),
]