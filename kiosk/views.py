from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, request
from kiosk.models import Recipe, Jumun

# Create your views here.

def index(response):
  return render(response,'kiosk/main.html')

def menu(response):
  menu_list = Recipe.objects.order_by()
  context = {'menu_list':menu_list}
  return render(response,'kiosk/menu.html',context)

def jumun_menu_h1(response):
  jumun = get_object_or_404(Jumun)
  if request.method == "POST":
    jumun.count.add(request)
    return redirect('kiosk:menu')
  else:
    messages.error(request, '수정권한이 없습니다')


# @login_required(login_url='common:login')
# def answer_create(request,question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   if request.method == "POST":
#     form = AnswerForm(request.POST)
#     if form.is_valid():
#       answer = form.save(commit=False)
#       answer.question = question
#       answer.create_date = timezone.now()
#       answer.author = request.user
#       answer.save()
#       return redirect('{}#answer_{}'.format(resolve_url('board:detail', question_id=question.id), answer.id))
#       # return redirect('board:detail', question_id=question.id)
#   else:
#     form = AnswerForm()
#   context = {'form':form, 'question':question}
#   return render(request,'board/detail.html',context)