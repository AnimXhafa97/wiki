from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('/new', views.new_page, name= 'new'),
    path('/save', views.save, name='save'),
    path("<str:title>", views.get_page, name="title"),
    path("/search", views.search, name = "search"),
]
