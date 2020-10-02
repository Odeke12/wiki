from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entry/<str:name>",views.entry, name="post"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"), 
    path("edit/<str:title>", views.edit, name="edit"),
    path("save/<str:title>", views.entry_save, name="save"),
    path("random", views.random, name="random")
]
