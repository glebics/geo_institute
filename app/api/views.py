from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.db import connections
from .serializers import StationSerializer
from rest_framework import serializers


def get_data_from_secondary_db(table_name):
    with connections['secondary'].cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        field_types = {name: serializers.CharField(
            max_length=255) for name in column_names}
        result = [dict(zip(column_names, row)) for row in rows]

    return result, field_types


def stations_json_view(request):
    data, field_types = get_data_from_secondary_db("stations")
    serializer = StationSerializer(data=data, fields=field_types, many=True)
    serializer.is_valid()
    serialized_data = serializer.data

    return JsonResponse({'data': serialized_data})


def station_coordinates_json_view(request):
    data, field_types = get_data_from_secondary_db("station_coordinates")
    serializer = StationSerializer(data=data, fields=field_types, many=True)
    serializer.is_valid()
    serialized_data = serializer.data

    return JsonResponse({'data': serialized_data})


def files_json_view(request):
    data, field_types = get_data_from_secondary_db("files")
    serializer = StationSerializer(data=data, fields=field_types, many=True)
    serializer.is_valid()
    serialized_data = serializer.data

    return JsonResponse({'data': serialized_data})


# def get_data_from_secondary_db():
#     with connections['secondary'].cursor() as cursor:
#         cursor.execute("SELECT * FROM stations")
#         rows = cursor.fetchall()
#     return rows


# def test_view(request):
#     data = get_data_from_secondary_db()
#     return JsonResponse({'data': data})

def fullness_view(request, station_name):
    # Пример данных
    start_period = "001 2000"
    end_period = "010 2000"
    data = [
        ("2000 001", "100%"),
        ("2000 002", "100%"),
        ("2000 003", "100%"),
        ("2000 004", "100%"),
        ("2000 005", "100%"),
        ("2000 006", "100%"),
        ("2000 007", "100%"),
        ("2000 008", "100%"),
        ("2000 009", "100%"),
        ("2000 010", "100%"),
    ]

    context = {
        'start_period': start_period,
        'end_period': end_period,
        'station_name': station_name,
        'data': data,
    }
    return render(request, 'fullness.html', context)


def archive_access_view(request):
    stations = [
        "artu", "yssk", "mago", "mobn", "lovi", "pet", "yaka",
        "petp", "yakz", "tixg", "tixi", "magi", "petp", "yakt", "yakt",
        "irkm", "mobi", "nril", "nri", "petr", "yakz", "bili", "pets",
        "tixi", "yaka", "nril", "pets", "yssk", "petr", "bilb", "irk",
        "kslv", "nurg", "svet"
    ]
    years = list(range(1997, 2024))  # Пример диапазона годов

    context = {
        'stations': stations,
        'years': years
    }
    return render(request, 'archive_access.html', context)


def process_archive_request(request):
    if request.method == 'POST':
        selected_stations = request.POST.getlist('stations')
        data_type = request.POST.get('data_type')
        start_year = request.POST.get('start_year')
        end_year = request.POST.get('end_year')
        day_of_year = request.POST.get('day_of_year')
        request_type = request.POST.get('request_type')

        # Здесь можно обработать данные формы, например, сохранить их в базе данных или выполнить нужные действия
        return HttpResponse(f"Stations: {selected_stations}, Data type: {data_type}, Period: {start_year}-{end_year}, Day of year: {day_of_year}, Request type: {request_type}")

    return redirect('archive_access')


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
