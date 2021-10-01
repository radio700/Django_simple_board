from django.core.checks import messages
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from board.models import Question,Answer, Comment
from board.forms import AnswerForm, QuestionForm, CommentForm
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


@login_required(login_url='common:login')
def comment_create_question(request,question_id):
  question = get_object_or_404(Question,pk=question_id)
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.author = request.user
      comment.create_date = timezone.now()
      comment.question = question
      comment.save()
      return redirect('board:detail', question_id=question.id)
  else:
    form = CommentForm()
  context = {'form':form, 'question':question}
  return render(request,'board/comment_form.html',context)


@login_required(login_url='common:login')
def comment_modify_question(request,comment_id):
  comment = get_object_or_404(Comment,pk=comment_id)
  if request.method == "POST":
    form = CommentForm(request.POST, instance=comment)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.modify_date = timezone.now()
      comment.save()
      return redirect('board:detail', question_id=comment.question.id)
  else:
    form = CommentForm(instance=comment)
  context = {'form': form}
  return render(request, 'board/comment_form.html', context) 

@login_required(login_url='common:login')
def comment_delete_question(request,comment_id):
  comment = get_object_or_404(Comment,pk=comment_id)
  if request.user != comment.author:
    messages.error(request,'삭제권한없음')
    return redirect('board:detail', question_id=comment.question.id)
  else:
    comment.delete()
  return redirect('board:detail',question_id=comment.question.id)


@login_required(login_url='common:login')
def comment_create_answer(request,answer_id):
  answer = get_object_or_404(Answer,pk=answer_id)
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.author = request.user
      comment.create_date = timezone.now()
      comment.answer = answer
      comment.save()
      return redirect('board:detail', question_id=comment.answer.question.id)
  else:
    form = CommentForm()
  context = {'form':form}
  return render(request, 'board/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_answer(request,comment_id):
  comment = get_object_or_404(Comment,pk=comment_id)

  if request.user != comment.author:
    messages.error(request,'수정권한없음')
    return redirect('board:detail', question_id = comment.answer.question.id)

  if request.method == "POST":
    form = CommentForm(request.POST, instance=comment)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.modify_date = timezone.now()
      comment.save()
      return redirect('board:detail', question_id=comment.answer.question.id)
  else:
    form = CommentForm(instance=comment)
  context = {'form':form}
  return render(request,'board/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_answer(request,comment_id):
  comment = get_object_or_404(Comment,pk=comment_id)
  
  if request.user != comment.author:
    messages.error(request,'삭제불가')
    return redirect('board:detail', question_id = comment.answer.question.id)

  else:
    comment.delete()
  return redirect('board:detail', question_id=comment.answer.question.id)