from django import forms
from kiosk.models import Recipe,Jumun

class RecipeForm(forms.ModelForm):
  class Meta:
    model = Recipe
    fields = ['menu_name','menucode','price']
    labels = {'menu_name':'메뉴이름','menucode':'메뉴코드','price':'가격'}

class JumunForm(forms.ModelForm):
  class Meta:
    model = Jumun
    fields = ['today_jumun_order','count','customer_id','jumun_date','menucode_id']
    labels = {
      'today_jumun_order':'오늘주문 수',
      'count':'총수',
      'customer_id':'유저이름',
      'jumun_date':'주문날자',
      'menucode_id':'메뉴코드'
      }
