from django.urls import path
from . import views

# url pattern 정의
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>", views.todo_list_id, name="TodoList-id"),
    path("<str:name>", views.todo_list_name, name="TodoList-name"),
]
