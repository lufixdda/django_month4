from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms


def create_todo_view(request):
    if request.method == "POST":
        form_todo = forms.TodoForm(request.POST, request.FILES)
        if form_todo.is_valid():
            form_todo.save()
            return redirect('/todo_list/')
    else:
        form_todo = forms.TodoForm()
    return render(request, 'create_todo.html', {'form': form_todo})


def read_todo_view(request):
    if request.method == "GET":
        todo_list = models.Todo.objects.all().order_by('-id')
    return render(request, 'todo_list.html', {'todo_list': todo_list})


def update_todo_view(request, id):
    todo_id = get_object_or_404(models.Todo, id=id)
    if request.method == "POST":
        form_todo = forms.TodoForm(request.POST, request.FILES, instance=todo_id)
        if form_todo.is_valid():
            form_todo.save()
            return redirect('/todo_list/')
    else:
        form_todo = forms.TodoForm(instance=todo_id)
    return render(request, 'update_todo.html', {'form': form_todo})


def delete_todo_view(request, id):
    todo_id = get_object_or_404(models.Todo, id=id)
    todo_id.delete()
    return redirect('/todo_list/')