from django.urls import path
from .views import signup_view, login_view, home_view, about_view, contact_view, logout_view, test_view


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),  # Ваше представление главной страницы
    path('about/', test_view, name='about'),
    path('contact/', test_view, name='contact'),
]
