from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.db import connections


def get_data_from_secondary_db():
    with connections['secondary'].cursor() as cursor:
        cursor.execute("SELECT * FROM stations")
        rows = cursor.fetchall()
    return rows


def test_view(request):
    data = get_data_from_secondary_db()
    return JsonResponse({'data': data})


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)  # Вывод ошибок формы в консоль для отладки
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Перенаправление на главную страницу после входа
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')  # Перенаправление на главную страницу после выхода


def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contact.html')
