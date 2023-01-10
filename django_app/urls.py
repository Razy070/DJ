"""
Login and logout views for the browsable API.

Add these to your root URLconf if you're using the browsable API and
your API requires authentication:

    urlpatterns = [
        ...
        path('auth/', include('rest_framework.urls'))
    ]

You should make sure your authentication settings include `SessionAuthentication`.
"""
from django.contrib.auth import views
from django.urls import path, include

app_name = 'rest_framework'
urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='rest_framework/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', include('django_app.urls')),
    path('', views.PasswordChangeDoneView, name=''),
    path('', views.PasswordChangeView, name=''),
    path('', views.PasswordResetCompleteView, name=''),
    path('', views.PasswordResetConfirmView, name=''),
    path('', views.PasswordResetDoneView, name=''),
    path('', views.PasswordResetView, name=''),
    path('', views.PasswordContextMixin, name=''),
    path('', views.LogoutView, name=''),
    path('', views.LoginView, name=''),
    path('', views.RedirectURLMixin, name=''),

]
