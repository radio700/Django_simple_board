from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from board.models import Question,Answer
from board.forms import AnswerForm, QuestionForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
  question_list = Question.objects.order_by('-create_date')
  page_match_page = request.GET.get('page')
  one_page_dang = Paginator(question_list,10)
  page_obj = one_page_dang.get_page(page_match_page)
  context = {'question_list':page_obj}
  return render(request,'board/index.html',context)

def detail(request,question_id):
  question = get_object_or_404(Question, pk=question_id)
  context = {"question":question}
  return render(request,'board/detail.html',context)

@login_required(login_url='common:login')
def answer_create(request,question_id):
  question = get_object_or_404(Question, pk=question_id)
  if request.method == "POST":
    form = AnswerForm(request.POST)
    if form.is_valid():
      answer = form.save(commit=False)
      answer.question = question
      answer.create_date = timezone.now()
      answer.author = request.user
      answer.save()
      return redirect('board:detail', question_id=question.id)
  else:
    form = AnswerForm()
  context = {'form':form, 'question':question}
  return render(request,'board/detail.html',context)

@login_required(login_url='common:login')
def question_create(request):
  if request.method == "POST":
    form = QuestionForm(request.POST)
    if form.is_valid():
      question = form.save(commit=False)
      question.create_date = timezone.now()
      question.author = request.user
      question.save()
      return redirect('board:index')
  else:
    form = QuestionForm()
  context = {'form':form}
  return render(request,'board/question_create.html',context)