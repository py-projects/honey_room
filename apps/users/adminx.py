# -*- coding:utf-8 -*-
import xadmin
from users.models import EmailPro
from xadmin import views


# 主题
class BaseSetting(object):
    enable_themes = True  # 打开主题功能
    use_bootswatch = True


# 针对全局的
class GlobelSettings(object):
    site_title = "honey_room后台管理系统"  # 修改页头
    site_footer = "甜甜屋"  # 修改页教
    menu_style = "accordion"  # 将菜单栏收起来
    apps_label_title = {
        'main': '商品管理',
        'users': '用户管理'
    }


class EmailVerifyRecordAdmin(object):
    # 设置xadmin后台显示字段
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 设置xadmin后台搜索字段，注意：搜索字段如果有时间类型会报错
    search_fields = ['code', 'email', 'send_type']
    # 设置xadmin后台过滤器帅选字段，时间用过滤器来做
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailPro, EmailVerifyRecordAdmin)  # 将数据表注册到xadmin后台显示
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobelSettings)
