from django.urls import path
from .views import todo_list_app_home, submit_todo, complete_todo, delete_todo

urlpatterns = [
    path('', todo_list_app_home, name='to_do_list_app_home'),
    path('submit_todo', submit_todo, name='submit_todo'),
    path('<int:pk>/complete_todo', complete_todo, name='complete_todo'),
    path('<int:pk>/delete_todo', delete_todo, name='delete_todo'),
]