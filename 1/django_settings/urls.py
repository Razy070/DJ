from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path
# from .views import index
from todo_app import views

# from .views import post


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')),
    path("footer/", include),
    path("home/", include),
]
