from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')
urlpatterns = router.urls + [
    path('api/todos/create/', TodoViewSet.as_view({'post': 'create_todo'}), name='create_todo'),
    path('api/todos/<int:pk>/delete/', TodoViewSet.as_view({'delete': 'delete_todo'}), name='delete_todo'),
    path('api/todos/<int:pk>/reorder/', TodoViewSet.as_view({'put': 'reorder_todo'}), name='reorder_todo'),
]
