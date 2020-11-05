from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='index'),
    path('register', views.register, name='index'),
    path('profile', views.profile, name='index'),
]