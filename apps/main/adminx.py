# from django.contrib import admin
import xadmin
from main.models import *


# menu_style = 'accordion'    #菜单折叠
#     # 搜索模型
#     global_search_models = [Tag, Art]
#
#     # 模型的图标(参考bootstrap图标插件)
#     global_models_icon = {
#         Art: "glyphicon glyphicon-book",
#         Tag: "fa fa-cloud"
#     }  # 设置models的全局图标


# Register your models here.
class CakeAdmin(object):
    # 后台列表显示列
    list_display = ['cake_name', 'cake_price', 'cake_number', 'cake_discount',
                    'cake_categories', 'cake_theme', 'cake_flavour', 'cake_weight', 'cake_relation']
    # 后台列表查询条件
    search_fields = ['cake_name']
    list_per_page = 10


xadmin.site.register(Cake, CakeAdmin)


class RelationAdmin(object):
    # 后台列表显示列
    list_display = ['relation', 'is_active']
    # 后台列表查询条件
    search_fields = ['relation']
    list_per_page = 10


xadmin.site.register(Relation, RelationAdmin)


class WeightAdmin(object):
    # 后台列表显示列
    list_display = ['weight', 'is_active']
    # 后台列表查询条件
    search_fields = ['weight']
    list_per_page = 10


xadmin.site.register(Weight, WeightAdmin)


class FlavourAdmin(object):
    # 后台列表显示列
    list_display = ['flavour', 'is_active']
    # 后台列表查询条件
    search_fields = ['flavour']
    list_per_page = 10


xadmin.site.register(Flavour, FlavourAdmin)


class ThemeAdmin(object):
    # 后台列表显示列
    list_display = ['theme', 'is_active']
    # 后台列表查询条件
    search_fields = ['theme']
    list_per_page = 10


xadmin.site.register(Theme, ThemeAdmin)


class CategoriesAdmin(object):
    # 后台列表显示列
    list_display = ['categories', 'is_active']
    # 后台列表查询条件
    search_fields = ['categories']
    list_per_page = 10


xadmin.site.register(Categories, CategoriesAdmin)
