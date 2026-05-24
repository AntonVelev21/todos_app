from django.urls import path

from todos.views import ListCreateTodosApiView, ListCategoriesApiView, RetrieveUpdateTodoApiView

urlpatterns = [
    path('', ListCreateTodosApiView.as_view(), name='todos'),
    path('<int:pk>/', RetrieveUpdateTodoApiView.as_view(), name='todos-details'),
    path('categories/', ListCategoriesApiView.as_view(), name='categories')
]