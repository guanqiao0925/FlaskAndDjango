from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, 'myapp/index.html')
    # return HttpResponse('hello world')


# 首页
def home(request):
    # 取session
    username = request.session.get('name', '游客')
    return render(request, 'myapp/home.html', {'username': username})
    # return redirect('/app/login')

# 登陆
def login(request):
    return render(request, 'myapp/login.html')

# 重定向 首页 显示用户名
def showhome(request):
    username = request.POST.get('username')
    # 存session
    request.session['name'] = username
    return redirect('/app/home')

# 退出登陆 清空session
from django.contrib.auth import logout
def quit(request):
    logout(request)
    # request.session.clear()
    # request.session.flush()
    return redirect('/app/home')