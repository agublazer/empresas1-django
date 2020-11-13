from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  
from app.models import WeekMenu


class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=128)
    reference = models.CharField(max_length=128)
    gender = models.CharField(max_length=20)
    exercise = models.CharField(max_length=20)
    birth = models.DateField()
    weight = models.FloatField()
    height = models.FloatField()
    calories = models.IntegerField()
    goal = models.CharField(max_length=30)
    health_condition = models.CharField(max_length=30)
    week_menu = models.ForeignKey(WeekMenu, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.user.first_name

    def save(self, *args, **kwargs): 
        max_cal_menu = self.calories * 4/10
        min_cal_menu = self.calories * 35/100
        menu = WeekMenu.objects.filter(monday_calories__gte=min_cal_menu,monday_calories__lte=max_cal_menu).first()
        print(menu)
        self.week_menu = menu
        super(Client, self).save(*args, **kwargs) 

class Membership(models.Model):
    date = models.DateField(default=datetime.now)
    client = models.OneToOneField(Client,on_delete=models.CASCADE)
    period = models.CharField(max_length=20)
