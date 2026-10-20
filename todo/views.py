from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from . import models, forms


class CreateTodoView(CreateView):
    form_class = forms.TodoForm
    template_name = 'create_todo.html'
    success_url = reverse_lazy('todo_list')


class ReadTodoView(ListView):
    model = models.Todo
    template_name = 'todo_list.html'
    context_object_name = 'todo_list'
    ordering = ['-id']


class UpdateTodoView(UpdateView):
    model = models.Todo
    form_class = forms.TodoForm
    template_name = 'update_todo.html'
    success_url = reverse_lazy('todo_list')


class DeleteTodoView(DeleteView):
    model = models.Todo
    success_url = reverse_lazy('todo_list')
