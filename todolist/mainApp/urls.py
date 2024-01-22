# todo/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/todos/create/', TodoViewSet.as_view({'post': 'create_todo'}), name='create_todo'),
]
