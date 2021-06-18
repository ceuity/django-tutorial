from django.urls import path
from . import views

# url pattern 정의
urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>", views.index, name="index"),
    path("create/", views.create, name="create"),
]
