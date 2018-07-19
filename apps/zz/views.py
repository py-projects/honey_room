from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from main.models import Cake, CheckOut
from users.models import UserPro
from users.views import user_login


def tj_shopping(request):  # 添加购物车
    if request.user.is_authenticated:
        user_id = request.COOKIES.get('user_id')
        cake_id = request.GET.get('cake_id')
        number = request.GET.get('number')
        obj = CheckOut.objects.create(cake_id=cake_id,user_id=user_id,number=number)
        obj.save()
        user_name = UserPro.objects.filter(id=user_id).first().username

        cake_name = Cake.objects.filter(id=cake_id).first().cake_name

        return JsonResponse({'msg':'添加商品成功','user_name':user_name,'cake_name':cake_name})

    return redirect(reverse(user_login))



