from django.urls import path
from .views import index, properties, search, landlord, property_detail

urlpatterns = [
    path('', index, name="index"),
    path('properties/', properties, name="properties"),
    path('properties/<int:id>/', property_detail, name="property"),
    path('search_results/', search, name="search"),
    path('landlord/', landlord, name="landlord")
]