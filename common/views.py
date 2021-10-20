from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.http import HttpResponse
from common.forms import UserForm
# Create your views here.

def signup(request):
  if request.method == "POST":
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get("username")
      raw_pass = form.cleaned_data.get("password1")
      user = authenticate(username=username, password=raw_pass)
      login(request,user)
      return redirect('index')
  else:
    form = UserForm()
  context = {'form':form}
  return render(request,'common/signup.html',context)

def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, 'common/404.html', {})
