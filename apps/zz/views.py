from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from main.models import Cake, CheckOut
from users.models import UserPro
from users.views import user_login


def tj_shopping(request):  # 添加购物车
    if request.user.is_authenticated:
        print('用户已登陆')
        user_id = request.COOKIES.get('user_id')
        cake_id = request.GET.get('cake_id')
        number = request.GET.get('number')
        obj = CheckOut.objects.create(cake_id=cake_id, user_id=user_id, number=number)
        obj.save()
        user_name = UserPro.objects.filter(id=user_id).first().username

        cake_name = Cake.objects.filter(id=cake_id).first().cake_name

        return JsonResponse({'msg': '添加商品成功', 'user_name': user_name, 'cake_name': cake_name})
    print('用户未登录')
    return JsonResponse({'msg': '请先进行登陆!'})


def checkout(request):  # 购物车页面
    if request.user.is_authenticated:
        user_id = request.COOKIES.get('user_id')
        user_name = UserPro.objects.filter(id=user_id).first().username
        checkout = CheckOut.objects.filter(user_id=user_id)
        lis = []
        for i in checkout:
            dic = {}
            cake_id = i.cake_id
            number = i.number  # 物品数量
            imgs = Cake.objects.filter(id=cake_id).first().cake_img
            img = imgs.split(',')[0]  # 物品图片
            cake_name = Cake.objects.filter(id=cake_id).first().cake_name  # 物品名称
            cake_discount = Cake.objects.filter(id=cake_id).first().cake_discount
            f_cake_discount = float(cake_discount) * int(number)  # 价格
            dic['number'] = number
            dic['img'] = img
            dic['cake_name'] = cake_name
            dic['f_cake_discount'] = f_cake_discount
            lis.append(dic)

        return render(request, 'checkout.html', {'lis': lis, 'user_name': user_name})
    else:
        return redirect('/logout/')
