from django.contrib import admin
from django.urls import path
# from .views import index
from todo_app import views
# from .views import post

urlpatterns = [
    path("", views.index),
    path("contacts/", views.contacts),
]



