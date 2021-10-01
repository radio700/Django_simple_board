from django.core.checks import messages
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from board.models import Question,Answer
from board.forms import AnswerForm
from django.contrib.auth.decorators import login_required

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
def answer_modify(request,answer_id):
  answer = get_object_or_404(Answer, pk=answer_id)
  if request.user != answer.author:
      messages.error(request, '수정권한이 없습니다')
      return redirect('pybo:detail', question_id=answer.question.id)

  if request.method == "POST":
      form = AnswerForm(request.POST, instance=answer)
      if form.is_valid():
          answer = form.save(commit=False)
          answer.modify_date = timezone.now()
          answer.save()
          return redirect('board:detail', question_id=answer.question.id)
  else:
      form = AnswerForm(instance=answer)
  context = {'answer': answer, 'form': form}
  return render(request, 'board/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request,answer_id):
  answer = get_object_or_404(Answer,pk=answer_id)
  if request.user != answer.author:
    messages.error(request,'삭제못함')
  else:
    answer.delete()
  return redirect('board:detail', question_id=answer.question.id)