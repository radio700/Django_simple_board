from django.urls import path, include
from . import views

app_name = 'kiosk'

# 127.0.0.0/kiosk/

urlpatterns = [
  path('',views.index, name='index'),
  path('menu/',views.menu, name='menu'),
  path('jumun/menu/h1/',views.jumun_menu_h1, name='jumun_menu_h1'),
  
]