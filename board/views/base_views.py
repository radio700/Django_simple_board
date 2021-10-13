from django.shortcuts import get_object_or_404, render
from board.models import Question
from django.core.paginator import Paginator

# Create your views here.

def index(request):
  question_list = Question.objects.order_by('-create_date')
  page_match_page = request.GET.get('page')
  one_page_dang = Paginator(question_list,15)
  page_obj = one_page_dang.get_page(page_match_page)
  context = {'question_list':page_obj}
  return render(request,'board/index.html',context)

def detail(request,question_id):
  question = get_object_or_404(Question, pk=question_id)
  context = {"question":question}
  return render(request,'board/detail.html',context)