from django.shortcuts import render
from main.models import *


# Create your views here.
def products(request):
    argument = request.GET
    feild = argument.get('key')
    if argument is None:
        cakes = Cake.objects.all()
    elif feild == 'cake_relation':
        cakes = Cake.objects.filter(cake_relation__relation=argument.get('value'))
    elif feild == 'cake_flavour':
        cakes = Cake.objects.filter(cake_flavour__flavour=argument.get('value'))
    elif feild == '':
        cakes = Cake.objects.filter(cake_weight__weight=argument.get('value'))
    pass