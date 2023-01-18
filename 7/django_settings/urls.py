from django.urls import path
# from hello import views
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path
# from .views import index
from django_app import views

urlpatterns = [
    path("", views.index),
    path("contacts/", views.contacts),
    path('admin/', admin.site.urls),
]
