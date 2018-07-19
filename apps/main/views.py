from django.shortcuts import render
from django.views import View

from main.models import *

# Create your views here.


def cake(request):
    argument = request.GET
    feild = argument.get('type')
    value = argument.get('value')
    if not argument:
        cakes = Cake.objects.all()
        return render(request, 'products.html', {'cakes': cakes,
                                                 'classify': '全部商品'})
    return None


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