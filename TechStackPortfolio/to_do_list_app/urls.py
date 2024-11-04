from django.urls import path
from .views import todo_list_app_home

urlpatterns = [
    path('', todo_list_app_home, name='to_do_list_app_home'),
]