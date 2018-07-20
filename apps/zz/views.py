import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from main.models import Cake, CheckOut
from users.models import UserPro
from users.views import user_login


def tj_shopping(request):  # 添加购物车
    if request.user.is_authenticated:  # 判断用户是否登录
        user_id = request.COOKIES.get('user_id')
        cake_id = request.GET.get('cake_id')
        number = request.GET.get('number')

        # 如果用户的商品为空，则添加
        if not CheckOut.objects.filter(user_id=user_id,cake_id=cake_id):
            CheckOut.objects.create(cake_id=cake_id,user_id=user_id,number=number)
        else:
            # 更新商品的数量
            CheckOut.objects.filter(user_id=user_id,cake_id=cake_id).update(number=number)


        user_name = UserPro.objects.filter(id=user_id).first().username
        cake_name = Cake.objects.filter(id=cake_id).first().cake_name

        return JsonResponse({'msg':'添加商品成功','user_name':user_name,'cake_name':cake_name})
    else:
        return redirect(reverse(user_login))  # 如果没有登录则重定向到登录页面


def checkout(request):  # 购物车页面
    if request.user.is_authenticated:  # 判断用户是否登录
        user_id = request.COOKIES.get('user_id')  # 获取用户的id
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
            f_cake_discount = float(cake_discount)*int(number) # 价格
            dic['number'] = number
            dic['img'] = img
            dic['cake_name'] = cake_name
            dic['f_cake_discount'] = f_cake_discount
            lis.append(dic)

        return render(request,'checkout.html',{'lis':lis,'user_name':user_name})
    else:
        return redirect(reverse(user_login))


def homepage(request):  # 主页面显示

    ids = Cake.objects.all().values('id')  # 获取所有id
    id_lis = []
    for i in ids:
        id_lis.append(i['id'])  # 将字典转换成列表

    # 得到一个随机值作为id_lis的索引
    d = id_lis[random.randint(0,len(id_lis))]
    d_cake = Cake.objects.filter(id=d).first()

    d_cake_name = d_cake.cake_name  # 物品名字
    d_cake_price = d_cake.cake_price  # 价格
    d_cake_img = d_cake.cake_img.split(',')[0]  # 图片


    x = id_lis[random.randint(0, len(id_lis))]
    x_cake = Cake.objects.filter(id=x).first()
    x_cake_name = x_cake.cake_name
    x_cake_price = x_cake.cake_price
    x_cake_img = x_cake.cake_img.split(',')[0]


    lis = []
    for i in range(8):
        dic = {}
        cake_id = id_lis[random.randint(0,len(id_lis))]
        cake = Cake.objects.filter(id=cake_id).first()
        cake_name = cake.cake_name
        cake_price = cake.cake_price
        cake_img = cake.cake_img.split(',')[0]
        dic['cake_name'] = cake_name
        dic['cake_price'] = cake_price
        dic['cake_img'] = cake_img
        dic['cake_id'] = cake_id
        lis.append(dic)
    return render(request,'index.html',{'lis':lis,'d_cake_name':d_cake_name,
                                        'd_cake_price':d_cake_price,
                                        'd_cake_img':d_cake_img,
                                        'd':d,
                                        'x_cake_name':x_cake_name,
                                        'x_cake_price':x_cake_price,
                                        'x_cake_img':x_cake_img,
                                        'x':x})