import hashlib
import uuid

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from users.models import UserPro


@csrf_exempt
def user_login(request):
    if request.method == "POST":
        #获取用户提交的用户名和密码
        user_name = request.POST.get("username","")
        pass_word = request.POST.get("password","")
        #成功返回user对象，失败None
        user = authenticate(username=user_name,password=pass_word)
        if user is not None:
            #登录
            login(request,user)
            return render(request,"index.html",{'username':user_name})
        else:
            return render(request,'index.html',{'msg':'用户名或密码错误'})

    elif request.method == "GET":
        return render(request, "index.html", {})

class LogoutView(View):
    '''用户登出'''
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


def crypt(pwd, cryptName='md5'):
    md5 = hashlib.md5()
    md5.update(pwd.encode())
    return md5.hexdigest()


def newToken(username):
    md5 = hashlib.md5()
    md5.update((str(uuid.uuid4())+username).encode())
    return md5.hexdigest()

@csrf_exempt
def register(request):
    if request.method == 'GET':
        print('222')
        return render(request,'account.html')
    print('11111')
    user = UserPro()
    user.username = request.POST.get('username')
    user.password = crypt(request.POST.get('password'))
    user.mobile = request.POST.get('moblie')
    user.nick_name = request.POST.get('nick_name')

    user.token = newToken(user.username)
    user.save()
    resp = redirect('/index/')
    resp.set_cookie('token',user.token)
    return resp

