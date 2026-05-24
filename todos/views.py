from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateAPIView

from todos.models import Todo, Category
from todos.serializers import TodoSerializer, CategorySerializer, TodoNestedSerializer


class ListCreateTodosApiView(ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        query_param = self.request.GET.get('category')
        if query_param:
            return Todo.objects.filter(category=query_param)
        return Todo.objects.all()


class RetrieveUpdateTodoApiView(RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class ListCategoriesApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

