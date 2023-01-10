from django.urls import path, re_path
from django_app import views

urlpatterns = [path('', views.home, name="stock-watcher-home"),
               path('stocks/', views.stock_search, name="stock-watcher-stocks"), ]
# path('about/', views.about, name="stock-watcher-about")]
