from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    #path('profile/', views.UserRegistrationView.as_view()),
]

