from django.shortcuts import render
from main.models import *

# Create your views here.


# 返回商品数据
def cake(request):
    cakes = None
    argument = request.GET
    field = argument.get('type')
    value = argument.get('value')
    if not argument:
        cakes = Cake.objects.all()
    elif field == 'cake_relation':
        cakes = Cake.objects.filter(cake_relation__relation=value)
    images = [x.cake_img.split(',') for x in cakes]
    cakes = zip(cakes, images)
    print(cakes, '------------------------------')
    return render(request, 'products.html', {'cakes': cakes,
                                             'classify': '全部商品'})
