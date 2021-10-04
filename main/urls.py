from django.urls import path
from main import views

app_name = 'main'

# 127.0.0.0/board/

urlpatterns = [
    path('', views.index, name='index'),
]
