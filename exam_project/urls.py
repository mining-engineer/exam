# exam_project/urls.py

from django.contrib import admin
from django.urls import path, include
from .views import index  # Импорт функции index из views.py

urlpatterns = [
    path('', index, name='index'), # Настройка маршрута для главной страницы
    path('admin/', admin.site.urls), 
    path('login/', include('user_app.urls', namespace='user_app')),
    path('logout/', include('user_app.urls', namespace='user_app')),
]