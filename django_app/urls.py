from django.contrib import admin
from django.urls import path
# from .views import index
from django_app import views
# from .views import post

urlpatterns = [
    path('', views.index, name=''),
]
