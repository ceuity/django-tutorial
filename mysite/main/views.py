from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, Item

# Create your views here.

# urls 에서 사용할 함수 정의
def index(response):
    return HttpResponse("<h1>Hello World!</h1>")


def todo_list_id(response, id):
    ls = TodoList.objects.get(id=id)
    item = ls.item_set.get(id=1)
    return HttpResponse(f"<h1>{ls.name}</h1></br><h1>{item.text}</h1>")


def todo_list_name(response, name):
    ls = TodoList.objects.get(name=name)
    return HttpResponse("<h1>%s</h1>" % ls.name)
