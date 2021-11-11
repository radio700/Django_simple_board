from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
  return render(response,'kiosk/main.html')

def menu(response):
  return render(response,'kiosk/menu.html')