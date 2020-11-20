from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('assign_menu', views.assignMenu, name='assignMenu'),
    path('profile', views.profile, name='profile'),
    path('addmenu', views.AddMenu.as_view(), name='addmenu'),
    path('addrestaurant', views.AddRestaurant.as_view(), name='addrestaurant'),
    path('restaurant_profile', views.profile_restaurant, name='restaurant_profile'),
]
