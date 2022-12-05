from django.contrib import admin
from django.urls import path
from django_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name=''),
    path('my_api_one/<int:post_id>/', views.my_api_one),
    path('my_api/', views.my_api),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
