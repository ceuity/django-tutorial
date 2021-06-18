from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoList, Item
from .forms import CreateNewList

# Create your views here.

# urls 에서 사용할 함수 정의
def index(response, id):
    ls = TodoList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):  # list.html 에서 html tag의 name
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")

    return render(response, "main/list.html", {"ls": ls})


def home(response):
    return render(response, "main/home.html", {"name": "test"})


def create(response):
    if response.method == "POST":
        print(response.POST)
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = TodoList(name=n)
            t.save()

        return HttpResponseRedirect(f"/{t.id}")
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})
