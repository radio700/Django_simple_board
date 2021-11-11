from django.shortcuts import render
from django.http import HttpResponse
from kiosk.models import Recipe, Jumun
# Create your views here.

def index(response):
  return render(response,'kiosk/main.html')

def menu(response):
  menu_list = Recipe.objects.order_by()
  context = {'menu_list':menu_list}
  return render(response,'kiosk/menu.html',context)