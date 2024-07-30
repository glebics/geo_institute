from django.urls import path
from .views import (signup_view, login_view, home_view, logout_view,
                stations_json_view, station_coordinates_json_view,
                files_json_view, fullness_view)


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),
    path('fullness/<str:station_name>/', fullness_view, name='fullness'),

    path('stations/', stations_json_view, name='stations'),
    path('station_coordinates/', station_coordinates_json_view, name='station_coordinates'),
    path('files/', files_json_view, name='files'),
]
