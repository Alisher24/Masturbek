from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]