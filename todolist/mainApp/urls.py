from django.urls import path
from .views import TodoAPI

urlpatterns = [
    path('todos/', TodoAPI.as_view(), name='todo-list'),  # For creating todos
    path('todos/<int:pk>/', TodoAPI.as_view(), name='todo-detail'),  # For retrieving, updating, deleting todos
]
