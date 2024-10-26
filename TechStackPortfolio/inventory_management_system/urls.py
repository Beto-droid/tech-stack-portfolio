from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_management_system_home, name='inventory_management_system_home'),
]