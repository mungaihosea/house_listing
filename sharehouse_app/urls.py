from django.urls import path
from .views import index, properties, search, landlord, property_detail, login, sign_up, logout

urlpatterns = [
    path('', index, name="index"),
    path('properties/', properties, name="properties"),
    path('properties/<int:id>/', property_detail, name="property"),
    path('search_results/', search, name="search"),
    path('landlord/', landlord, name="landlord"),
    path('login/', login, name="login"),
    path('sign_up/', sign_up, name="sign_up"),
    path('logout/', logout, name = "logout")
]