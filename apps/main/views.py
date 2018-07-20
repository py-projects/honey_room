from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from main.models import *
from django.core.paginator import Paginator

# Create your views here.


# 返回商品数据
def cake(request):
    cakes = None
    argument = request.GET
    field = argument.get('type')
    value = argument.get('value')
    page = 1
    # 获取页数
    if argument.get('page'):
        page = argument.get('page')
    if field == 'categories':
        if value == '商城':
            cakes = Cake.objects.all().order_by('id')
        else:
            cakes = Cake.objects.filter(cake_categories__cake_type=value)

    elif field == 'cake_relation':
        cakes = Cake.objects.filter(cake_relation__relation=value).order_by('id')
    pt = Paginator(cakes, 9)
    cakes_page = pt.page(page)
    images = [x.cake_img.split(',') for x in cakes_page]
    cakes = zip(cakes_page, images)
    return render(request, 'products.html', {'cakes': cakes,
                                             'page': cakes_page,
                                             'classify': value})


# 返回顶部菜单数据
def head(request):
    print('------------------------开始工作')
    data = {}
    relation = serializers.serialize('json', Relation.objects.filter(is_active=True))
    flavour = serializers.serialize('json', Flavour.objects.filter(is_active=True))
    weight = serializers.serialize('json', Weight.objects.filter(is_active=True))
    theme = serializers.serialize('json', Theme.objects.filter(is_active=True))
    categories = Categories.objects.filter(is_active=True)
    data['relation'] = relation
    data['flavour'] = flavour
    data['weight'] = weight
    data['theme'] = theme

    categ = ['商城']
    for c in categories:
        categ.append(c.cake_type)
    data['type'] = categ

    return JsonResponse(data)


class CakeListView(View):
    #详情页
    def get(self,request):
        cake_id = request.GET.get("cake_id")
        cake = Cake.objects.get(id = cake_id)
        print(cake)
        img=Cake.objects.get(id=cake_id).cake_img
        i =img.replace('http://www.holiland.comhttp://www.holiland.com/','http://www.holiland.com/')
        cakeimgs = i.split(',')

        img_01 = Cake.objects.get(id=cake_id).cake_detail
        img_lis = img_01.split(',')

        cake_flavour = cake.cake_flavour
        if cake_flavour:
            tags = Cake.objects.filter(cake_flavour=cake_flavour)[:4]
        else:
            tags = []
        print(tags)

        return render(request, 'single.html',{"cake":cake,
                                              "cakeimgs":cakeimgs,
                                              'img_lis':img_lis,
                                              'tags':tags})
