from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from board.models import Question,Answer
from board.forms import AnswerForm
# Create your views here.

def index(request):
  question_list = Question.objects.order_by('-create_date')
  context = {'question_list':question_list}
  return render(request,'board/index.html',context)

def detail(request,question_id):
  question = get_object_or_404(Question, pk=question_id)
  context = {"question":question}
  return render(request,'board/detail.html',context)

def answer_create(request,question_id):
  question = get_object_or_404(Question, pk=question_id)
  if request.method == "POST":
    form = AnswerForm(request.POST)
    if form.is_valid():
      answer = form.save(commit=False)
      answer.question = question
      answer.create_date = timezone.now()
      answer.save()
      return redirect('board:detail', question_id=question.id)
  else:
    form = AnswerForm()
  context = {'form':form, 'question':question}
  return render(request,'board/detail.html',context)