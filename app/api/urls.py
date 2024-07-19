from django.urls import path
from .views import (signup_view, login_view, home_view, logout_view,
                stations_json_view, station_coordinates_json_view,
                files_json_view)


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),

    path('stations/', stations_json_view, name='stations'),
    path('api/station-coordinates/', station_coordinates_json_view, name='station_coordinates_json'),
    path('files/', files_json_view, name='files'),
]
