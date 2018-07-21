"""honey_room URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.views.generic import TemplateView

import xadmin
from django.urls import path
import main.views as main_views
from users import views
from users.views import LogoutView
from xadmin.plugins import xversion
import zz.views

# version模块自动注册需要版本控制的 Model
xversion.register_models()
xadmin.autodiscover()

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # 首页
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    # 登录
    path('index/', views.user_login, name='index'),
    # 登出
    path('logout/', LogoutView.as_view(), name="logout"),
    # 注册
    path('register/', views.register, name='register'),
    # 商品列表
    path('cake/', main_views.cake, name='cake'),

    path('more/', main_views.more_check, name='more'),

    path('tj_shopping/',zz.views.tj_shopping,name='ti_shopping'),

    path('checkout/',zz.views.checkout,name='checkout'),

    path('delect_view/',zz.views.delect_view,name='delect_view'),

    path('homepage/',zz.views.homepage,name='homepage'),

    # 请求顶部菜单
    path('head/', main_views.head, name='head'),
    # 商品详情页
    # path('cakelistview/(?P<cake_id>\d+)/$', main_views.CakeListView.as_view(), name ='cakelistview')
    path('cakelistview/', main_views.CakeListView.as_view(), name='cakelistview'),
    # 添加到购物车
    path('tj_shopping/', zz.views.tj_shopping, name='ti_shopping'),
    # 购物车页面
    path('checkout/', zz.views.checkout, name='checkout'),
]
