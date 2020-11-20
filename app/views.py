from django.shortcuts import render, redirect

# Create your views here.
# from django.http import HttpResponse
# from django.http import HttpResponseRedirect
from django.views import View
from .models import WeekMenu, Restaurant
from django.contrib.auth.decorators import login_required
from clients.models import Client
import datetime

global restaurant_name

def index(request):
	return render(request, 'index.html')


def login(request):
	return render(request, 'login.html')


def register(request):
	return render(request, 'register.html')


def profile_restaurant(request):
	return render(request, 'perfilrestaurante.html')

def assignMenu(request):
	current_user = request.user
	client = Client.objects.get(user=current_user)
	restaurant_name = request.session['restaurant_name']
	max_cal_menu = client.calories * 4/10
	min_cal_menu = client.calories * 35/100
	week_menu = WeekMenu.objects.filter(restaurant=restaurant_name,monday_calories__gte=min_cal_menu,monday_calories__lte=max_cal_menu).first()
	client.week_menu = week_menu
	client.save()
	return redirect('/profile')

@login_required
def profile(request):
	if request.method == 'GET':
		current_user = request.user
		client = Client.objects.get(user=current_user)
		week_menu = client.week_menu
		all_restaurants = Restaurant.objects.all()
		if week_menu:
			return render(request, 'profile.html', {'calories': client.calories, 'name': current_user.first_name, 'restaurants': all_restaurants, 'week_menu':week_menu,
			'monday': week_menu.monday, 'monday_calories': week_menu.monday_calories,
			'tuesday': week_menu.tuesday, 'tuesday_calories': week_menu.tuesday_calories,
			'wednesday': week_menu.wednesday, 'wednesday_calories': week_menu.wednesday_calories,
			'thursday': week_menu.thursday, 'thursday_calories': week_menu.thursday_calories,
			'friday': week_menu.friday, 'friday_calories': week_menu.friday_calories,
			'saturday': week_menu.saturday, 'saturday_calories': week_menu.saturday_calories})
		else:
			return render(request, 'profile.html', {'calories': client.calories, 'name': current_user.first_name, 'restaurants': all_restaurants, 'week_menu':week_menu})


	elif request.method == 'POST':
		all_restaurants = Restaurant.objects.all()
		current_user = request.user
		client = Client.objects.get(user=current_user)
		restaurant_name = request.POST.get("restaurant")
		request.session['restaurant_name'] = restaurant_name
		max_cal_menu = client.calories * 4/10
		min_cal_menu = client.calories * 35/100
		week_menu = WeekMenu.objects.filter(restaurant=restaurant_name,monday_calories__gte=min_cal_menu,monday_calories__lte=max_cal_menu).first()
		print(week_menu)
		if week_menu:
			return render(request, 'profile.html', {'calories': client.calories, 'name': current_user.first_name, 'restaurants': all_restaurants, 'form_week_menu':week_menu, 'restaurant_name':restaurant_name,
			'monday': week_menu.monday, 'monday_calories': week_menu.monday_calories,
			'tuesday': week_menu.tuesday, 'tuesday_calories': week_menu.tuesday_calories,
			'wednesday': week_menu.wednesday, 'wednesday_calories': week_menu.wednesday_calories,
			'thursday': week_menu.thursday, 'thursday_calories': week_menu.thursday_calories,
			'friday': week_menu.friday, 'friday_calories': week_menu.friday_calories,
			'saturday': week_menu.saturday, 'saturday_calories': week_menu.saturday_calories})
		else:
			return render(request, 'profile.html', {'calories': client.calories, 'name': current_user.first_name, 'restaurants': all_restaurants})


class AddMenu(View):
	def get(self, request, *args, **kwargs):
		all_menus = WeekMenu.objects.all()
		all_restaurants = Restaurant.objects.all()
		return render(request, 'restaurant-menu.html', {'success': None, 
			'all_menus': all_menus, 'restaurants': all_restaurants})

	def post(self, request, *args, **kwargs):
		restaurant_name = request.POST.get("restaurant")
		menu_name = request.POST.get("name")

		monday = request.POST.get("monday")
		monday_calories = request.POST.get("monday_calories")
		tuesday = request.POST.get("tuesday")
		tuesday_calories = request.POST.get("tuesday_calories")
		wednesday = request.POST.get("wednesday")
		wednesday_calories = request.POST.get("wednesday_calories")
		thursday = request.POST.get("thursday")
		thursday_calories = request.POST.get("thursday_calories")
		friday = request.POST.get("friday")
		friday_calories = request.POST.get("friday_calories")
		saturday = request.POST.get("saturday")
		saturday_calories = request.POST.get("saturday_calories")
		sunday = request.POST.get("sunday")
		sunday_calories = request.POST.get("sunday_calories")

		menu = WeekMenu(
			restaurant=restaurant_name,
			menu_name=menu_name,
			monday=monday,
			monday_calories=monday_calories,
			tuesday=tuesday,
			tuesday_calories=tuesday_calories,
			wednesday=wednesday,
			wednesday_calories=wednesday_calories,
			thursday=thursday,
			thursday_calories=thursday_calories,
			friday=friday,
			friday_calories=friday_calories,
			saturday=saturday,
			saturday_calories=saturday_calories,
			sunday=sunday,
			sunday_calories=sunday_calories,
			begin_date=datetime.date.today()
		)
		menu.save()

		all_menus = WeekMenu.objects.all()
		all_restaurants = Restaurant.objects.all()

		return render(request, 'restaurant-menu.html', 
			{'success': True, 'all_menus': all_menus, 'restaurants': all_restaurants})


class AddRestaurant(View):
	def get(self, request, *args, **kwargs):
		all_restaurants = Restaurant.objects.all()
		return render(request, 'add-restaurant.html', {'success': None, 'all_restaurants': all_restaurants})

	def post(self, request, *args, **kwargs):
		restaurant_name = request.POST.get("restaurant")
		restaurant_address = request.POST.get("restaurant_address")
		restaurant_phone = request.POST.get("restaurant_phone")
		restaurant_cellphone = request.POST.get("restaurant_cellphone")
		restaurant_fb = request.POST.get("restaurant_fb")

		restaurant = Restaurant(
			name=restaurant_name,
			address=restaurant_address,
			phone=restaurant_phone,
			cellphone=restaurant_cellphone,
			fb_link=restaurant_fb
		)
		restaurant.save()

		all_restaurants = Restaurant.objects.all()

		return render(request, 'add-restaurant.html', {'success': True, 'all_restaurants': all_restaurants})
