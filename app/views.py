from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# from django.http import HttpResponseRedirect
from django.views import View
from .models import WeekMenu
from django.contrib.auth.decorators import login_required
from clients.models import Client
import datetime


def index(request):
	return render(request, 'index.html')


def login(request):
	return render(request, 'login.html')


def register(request):
	return render(request, 'register.html')

@login_required
def profile(request):
	current_user = request.user
	client = Client.objects.get(user=current_user)
	return render(request, 'profile.html',{'calories':client.calories,'name':current_user.first_name,
	'monday':client.week_menu.monday,'monday_calories':client.week_menu.monday_calories,
	'tuesday':client.week_menu.tuesday,'tuesday_calories':client.week_menu.tuesday_calories,
	'wednesday':client.week_menu.wednesday,'wednesday_calories':client.week_menu.wednesday_calories,
	'thursday':client.week_menu.thursday,'thursday_calories':client.week_menu.thursday_calories,
	'friday':client.week_menu.friday,'friday_calories':client.week_menu.friday_calories,
	'saturday':client.week_menu.saturday,'saturday_calories':client.week_menu.saturday_calories})


class AddMenu(View):
	def get(self, request, *args, **kwargs):
		all_menus = WeekMenu.objects.all()
		return render(request, 'restaurant-menu.html', {'success': None, 'all_menus': all_menus})

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

		return render(request, 'restaurant-menu.html', {'success': True, 'all_menus': all_menus})
