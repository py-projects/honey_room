import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from main.models import Cake, CheckOut
from users.models import UserPro


def tj_shopping(request):  # 添加购物车

    if request.user.is_authenticated:  # 判断用户是否登录
        user_id = request.COOKIES.get('user_id')
        cake_id = request.GET.get('cake_id')
        number = request.GET.get('number')
        car = CheckOut.objects.filter(user_id=user_id, cake_id=cake_id)
        # 如果用户的商品为空，则添加
        if not car:
            CheckOut.objects.create(cake_id=cake_id, user_id=user_id, number=number)
        else:
            print('--------------------购物车中的原数量：', car.first().number)
            number = int(car.first().number) + int(number)
            # 更新商品的数量
            CheckOut.objects.filter(user_id=user_id,cake_id=cake_id).update(number=number)

        user_name = UserPro.objects.filter(id=user_id).first().username
        cake_name = Cake.objects.filter(id=cake_id).first().cake_name

        return JsonResponse({'msg': '添加商品成功', 'user_name': user_name, 'cake_name': cake_name})
    return JsonResponse({'msg': '请先进行登陆!'})


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
            f_cake_discount = float(cake_discount) * int(number)  # 价格
            cake_id = Cake.objects.filter(id=cake_id).first().id
            dic['number'] = number
            dic['img'] = img
            dic['cake_name'] = cake_name
            dic['f_cake_discount'] = f_cake_discount
            dic['cake_id'] = cake_id
            lis.append(dic)

        return render(request, 'checkout.html', {'lis': lis, 'user_name': user_name})
    else:
        return redirect('/logout/')


def delect_view(request):  # 购物车删除
    if request.user.is_authenticated:
        cake_id = request.GET.get('cake_id')
        user_id = request.COOKIES.get('user_id')
        user_id01 = CheckOut.objects.filter(user_id=user_id, cake_id=cake_id)
        if user_id01.exists():
            user_id01.delete()
        return render(request, 'checkout.html')
    return render(request, 'index.html')


def homepage(request):  # 主页面显示
    username1 = request.COOKIES.get('user_name')
    ids = Cake.objects.all().values('id')  # 获取所有id
    id_lis = []
    for i in ids:
        id_lis.append(i['id'])  # 将字典转换成列表

    # 得到一个随机值作为id_lis的索引

    d = id_lis[random.randint(0, len(id_lis) - 1)]
    d_cake = Cake.objects.filter(id=d).first()

    d_cake_name = d_cake.cake_name  # 物品名字
    d_cake_price = d_cake.cake_price  # 价格
    d_cake_img = d_cake.cake_img.split(',')[0]  # 图片

    x = id_lis[random.randint(0, len(id_lis) - 1)]
    x_cake = Cake.objects.filter(id=x).first()
    x_cake_name = x_cake.cake_name
    x_cake_price = x_cake.cake_price
    x_cake_img = x_cake.cake_img.split(',')[0]

    lis = []
    for i in range(8):
        dic = {}
        cake_id = id_lis[random.randint(0, len(id_lis) - 1)]
        cake = Cake.objects.filter(id=cake_id).first()
        cake_name = cake.cake_name
        cake_price = cake.cake_price
        cake_img = cake.cake_img.split(',')[0]
        dic['cake_name'] = cake_name
        dic['cake_price'] = cake_price
        dic['cake_img'] = cake_img
        dic['cake_id'] = cake_id
        lis.append(dic)

    return render(request, 'index.html', {'lis': lis, 'd_cake_name': d_cake_name,
                                          'd_cake_price': d_cake_price,
                                          'd_cake_img': d_cake_img,
                                          'd': d,
                                          'x_cake_name': x_cake_name,
                                          'x_cake_price': x_cake_price,
                                          'x_cake_img': x_cake_img,
                                          'x': x})


def shopping_money(request):  # 购物车物品数量和总价格
    if request.user.is_authenticated:
        user_id = request.COOKIES.get('user_id')
        checkout = CheckOut.objects.filter(user_id=user_id).all()
        num = []
        price = []
        for i in checkout:
            cake_id = i.cake_id
            nums = int(i.number)
            cake = Cake.objects.filter(id=cake_id).first()
            cake_price = cake.cake_discount
            sum_price = float(cake_price) * nums
            num.append(nums)
            price.append(sum_price)
        number = sum(num)
        cake_price = round(sum(price), 2)
        print(number, cake_price)
        return JsonResponse({'number': number, 'cake_price': cake_price})
    return JsonResponse({'msg': '请先登录'})
