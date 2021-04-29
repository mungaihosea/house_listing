from django.urls import path
from .views import index, properties, search, landlord, property_detail, login, sign_up, logout, edit_property

urlpatterns = [
    path('index/', index, name="index"),
    path('properties/', properties, name="properties"),
    path('properties/<int:id>/', property_detail, name="property"),
    path('search_results/', search, name="search"),
    path('landlord/', landlord, name="landlord"),
    path('', login, name="login"),
    path('sign_up/', sign_up, name="sign_up"),
    path('logout/', logout, name = "logout"),
    path('edit_property/<slug:id>/', edit_property, name="edit_property")
]