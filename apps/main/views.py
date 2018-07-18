from django.shortcuts import render
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