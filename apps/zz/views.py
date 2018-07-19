from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from main.models import Cake, CheckOut
from users.views import user_login


def checkout(request):  # 添加购物车
    print('已经进入了函数')
    if request.user.is_authenticated:
        user_id = request.COOKIES.get('user_id')
        cake_id = request.GET.get('cake_id')
        number = request.GET.get('number')
        obj = CheckOut.objects.create(cake_id=cake_id,user_id=user_id,number=number)
        obj.save()
        return redirect(reverse())

    return redirect(reverse(user_login))