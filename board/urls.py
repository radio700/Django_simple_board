from django.urls import path, include
from board import views

app_name = 'board'

# 127.0.0.0/board/

urlpatterns = [
    path('', views.index, name='index'),
]
