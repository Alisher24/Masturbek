from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.index, name='login'),
    path('profile/', views.profile, name='profile'),  # Добавленный путь для страницы профиля
    path('logout/', views.logout_view, name='logout'),
    path('', include('Home.urls'), name='home')
]

