from django.db import models

from users.models import UserPro


class Relation(models.Model):
    relation = models.CharField(max_length=20, verbose_name='关系')
    is_active = models.BooleanField(default=False, verbose_name='筛选')

    class Meta:
        verbose_name = "添加关系类型"
        verbose_name_plural = verbose_name


class Weight(models.Model):
    weight = models.CharField(max_length=20, verbose_name='重量')
    is_active = models.BooleanField(default=False, verbose_name='筛选')

    class Meta:
        verbose_name = "添加重量"
        verbose_name_plural = verbose_name


class Flavour(models.Model):
    flavour = models.CharField(max_length=20, verbose_name='口味')
    is_active = models.BooleanField(default=False, verbose_name='筛选')

    class Meta:
        verbose_name = "添加口味"
        verbose_name_plural = verbose_name


class Theme(models.Model):
    theme = models.CharField(max_length=20, verbose_name='主题')
    is_active = models.BooleanField(default=False, verbose_name='筛选')

    class Meta:
        verbose_name = "添加主题"
        verbose_name_plural = verbose_name


class Categories(models.Model):
    cake_type = models.CharField(max_length=20, verbose_name='类别')
    is_active = models.BooleanField(default=False, verbose_name='筛选')

    class Meta:
        verbose_name = "添加类别"
        verbose_name_plural = verbose_name


# 商品数据存储
class Cake(models.Model):
    cake_name = models.CharField(max_length=50, verbose_name='蛋糕名')
    cake_img = models.CharField(max_length=256, verbose_name='列表图')
    cake_price = models.CharField(max_length=10, verbose_name='原价', default=10000)
    cake_number = models.CharField(max_length=10, verbose_name='库存', default=1)
    cake_discount = models.CharField(max_length=10, verbose_name='现价', default=10000)
    cake_detail = models.TextField(verbose_name='详情')
    cake_relation = models.ForeignKey(Relation, on_delete=models.CASCADE, verbose_name='关系')
    cake_weight = models.ForeignKey(Weight, on_delete=models.CASCADE, verbose_name='重量')
    cake_flavour = models.ForeignKey(Flavour, on_delete=models.CASCADE, verbose_name='口味')
    cake_theme = models.ForeignKey(Theme, on_delete=models.CASCADE, verbose_name='主题')
    cake_categories = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='类别')

    class Meta:
        verbose_name = "添加蛋糕"
        verbose_name_plural = verbose_name


# 存储购物车数据
class CheckOut(models.Model):
    user = models.ForeignKey(UserPro, on_delete=models.CASCADE, verbose_name='用户')
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE, verbose_name='蛋糕')
    number = models.CharField(max_length=10, verbose_name='原价', default=1)

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name
