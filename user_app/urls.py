# user_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'user_app'

urlpatterns = [
    path('login/', views.user_login, name='login'),  # Страница входа
    path('logout/', views.user_logout, name='logout'),  # Страница выхода
]
