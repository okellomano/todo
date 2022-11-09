from django.urls import path
from . import views

# app_name = 'todos'
urlpatterns = [
    path('', views.TodoListView.as_view(), name='all_todos'),
    path('<int:pk>/', views.TodoDetailView.as_view(), name='todo_detail'),
]
