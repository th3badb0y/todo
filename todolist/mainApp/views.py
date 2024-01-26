from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer

class TodoAPI(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({'detail': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)
        
        todo.delete()
        return Response({'detail': 'Todo deleted successfully'})

    def put(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({'detail': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({'detail': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)

        order = request.data.get('order')
        if order is not None:
            todo.order = order
            todo.save()
            return Response({'detail': 'Todo reordered successfully'})
        return Response({'detail': 'Order not provided'}, status=status.HTTP_400_BAD_REQUEST)
