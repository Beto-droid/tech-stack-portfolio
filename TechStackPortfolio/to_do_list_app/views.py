from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Todo
from django.contrib.auth.models import User
from .forms import TodoForm
from django.views.decorators.http import require_POST, require_http_methods

@login_required
def todo_list_app_home(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(todo_user=request.user)
    else:
        public_user = User.objects.get(username="alberto")
        todos = Todo.objects.filter(todo_user=public_user)

    context = {
        'todos': todos,
        'form': TodoForm,
    }
    return render(request, 'to_do_list_app/to_do_list_app_home.html', context)


@login_required
@require_POST
def submit_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = form.save(commit=False)
        if not request.user.is_authenticated:
            request.user = User.objects.get(username="alberto")
        todo.todo_user = request.user
        todo.save()

        # Return an HTML partial
        context = {
            'todo': todo,
        }
        template_name = 'to_do_list_app/to_do_list_app_home.html'
        template_name += "#todo-item-partial"
        return render(request, template_name, context)

@login_required
@require_POST
def complete_todo(request, pk):
    if request.user.is_authenticated:
        todo = get_object_or_404(Todo, pk=pk, todo_user=request.user)
        todo.is_completed = True
        todo.save()
    else:
        public_user = User.objects.get(username="alberto")
        todo = get_object_or_404(Todo, todo_user=public_user, pk=pk)
        todo.is_completed = True
        todo.save()

    # Return an HTML partial
    context = {
        'todo': todo,
    }
    template_name = 'to_do_list_app/to_do_list_app_home.html'
    template_name += "#todo-item-partial"
    return render(request, template_name, context)

@login_required
@require_http_methods(['DELETE'])
def delete_todo(request, pk):
    if request.user.is_authenticated:
        todo = get_object_or_404(Todo, pk=pk, todo_user=request.user)
        todo.delete()
    else:
        public_user = User.objects.get(username="alberto")
        todo = get_object_or_404(Todo, todo_user=public_user, pk=pk)
        todo.delete()

    return HttpResponse()
