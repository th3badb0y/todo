# todo/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=['post'])
    def create_todo(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['delete'])
    def delete_todo(self, request, pk=None):
        todo = self.get_object()
        todo.delete()
        return Response({'detail': 'Todo deleted successfully'})

    @action(detail=True, methods=['put'])
    def reorder_todo(self, request, pk=None):
        todo = self.get_object()
        order = request.data.get('order')

        if order is not None:
            todo.order = order
            todo.save()

        return Response({'detail': 'Todo reordered successfully'})
