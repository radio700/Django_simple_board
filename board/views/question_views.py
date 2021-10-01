from django.core.checks import messages
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from board.models import Question
from board.forms import QuestionForm
from django.contrib.auth.decorators import login_required


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

@login_required(login_url='common:login')
def question_modify(request,question_id):
  question = get_object_or_404(Question, pk=question_id)
  if request.user != question.author:
      messages.error(request, '수정권한이 없습니다')
      return redirect('pybo:detail', question_id=question.id)

  if request.method == "POST":
    form = QuestionForm(request.POST, instance=question)
    if form.is_valid():
      question = form.save(commit=False)
      question.modify_date = timezone.now()
      question.save()
      return redirect('board:detail', question_id = question.id)
  else:
    form = QuestionForm(instance=question)
  context = {'form':form, 'question':question}
  return render(request,'board/question_create.html',context)

@login_required(login_url='common:login')
def question_delete(request,question_id):
  question = get_object_or_404(Question,pk=question_id)

  if request.user != question.author:
    messages.error(request,'삭제못함')
    return redirect('board:detail', question_id=question.id)
  else:
    question.delete()
  return redirect('board:index')