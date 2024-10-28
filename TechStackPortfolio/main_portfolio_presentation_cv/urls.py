from django.urls import path
from .views import cv_list, cv_add

urlpatterns = [
    path('', cv_list, name='cv_list'),
    path('add/', cv_add, name='cv_add'),
]