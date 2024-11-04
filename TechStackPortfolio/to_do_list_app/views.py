from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Todo
from django.contrib.auth.models import User

# Create your views here.
@login_required
def todo_list_app_home(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(todo_user=request.user)
    else:
        public_user = get_object_or_404(User, username="alberto")
        todos = Todo.objects.filter(todo_user=public_user)

    context = {'todos': todos}
    return render(request, 'to_do_list_app/to_do_list_app_home.html', context)