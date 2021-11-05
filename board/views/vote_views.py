from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Answer, Question


@login_required(login_url='common:login')
def vote_question(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  question.voter.add(request.user)
  return redirect('board:detail', question_id=question_id)

@login_required(login_url='common:login')
def devote_question(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  question.devoter.add(request.user)
  return redirect('board:detail', question_id=question_id)

@login_required(login_url='common:login')
def vote_answer(request, answer_id):
  answer = get_object_or_404(Answer,pk=answer_id)
  answer.voter.add(request.user)
  return redirect('board:detail', question_id=answer.question.id)

@login_required(login_url='common:login')
def devote_answer(request, answer_id):
  answer = get_object_or_404(Answer,pk=answer_id)
  answer.devoter.add(request.user)
  return redirect('board:detail', question_id=answer.question.id)