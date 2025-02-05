#user_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    """Страница входа"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Перенаправление на главную страницу после входа
    else:
        form = AuthenticationForm()
    return render(request, 'logging/login.html', {'form': form})


@login_required
def user_logout(request):
    """Страница выхода"""
    logout(request)
    return render(request, 'logging/logout.html')