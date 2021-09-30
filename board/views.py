from django.shortcuts import render
from django.http import HttpResponse
from board.models import Question,Answer
# Create your views here.

def index(request):
  question_list = Question.objects.order_by('-create_date')
  context = {'question_list':question_list}
  return render(request,'board/index.html',context)