from django.http import JsonResponse
from django.shortcuts import render
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
        cakes = Cake.objects.all().order_by('id')
    elif field == 'cake_relation':
        cakes = Cake.objects.filter(cake_relation__relation=value).order_by('id')
    pt = Paginator(cakes, 9)
    cakes_page = pt.page(page)
    images = [x.cake_img.split(',') for x in cakes_page]
    cakes = zip(cakes_page, images)
    return render(request, 'products.html', {'cakes': cakes,
                                             'page': cakes_page,
                                             'classify': '全部商品'})


# 返回顶部菜单数据
def head(request):
    print('------------------------开始工作')
    data = {}
    relation = Relation.objects.filter(is_active=True)
    flavour = Flavour.objects.filter(is_active=True)
    weight = Weight.objects.filter(is_active=True)
    theme = Theme.objects.filter(is_active=True)
    categories = Categories.objects.filter(is_active=True)

    # 序列化
    relations = []
    for rel in relation:
        relations.append(rel.relation)

    data['关系'] = relations

    flavours = []
    for fla in flavour:
        flavours.append(fla.flavour)
    data['口味'] = flavours

    weights = []
    for w in weight:
        weights.append(w.weight)
    data['大小'] = weights

    themes = []
    for t in theme:
        themes.append(t.theme)
    data['主题'] = themes

    categ = ['商城']
    for c in categories:
        categ.append(c.cake_type)
    data['type'] = categ

    return JsonResponse(data)
