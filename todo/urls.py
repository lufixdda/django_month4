from django.urls import path
from . import views

urlpatterns = [
    path('todo_list/', views.ReadTodoView.as_view(), name='todo_list'),
    path('todo_list/<int:pk>/update/', views.UpdateTodoView.as_view(), name='todo_update'),
    path('todo_list/<int:pk>/delete/', views.DeleteTodoView.as_view(), name='todo_delete'),
    path('create_todo/', views.CreateTodoView.as_view(), name='todo_create'),
]
