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
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('index/', views.user_login, name='index'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', views.register, name='register'),
    # 商品列表
    path('cake/', main_views.cake, name='cake'),
    path('tj_shopping/',zz.views.tj_shopping,name='ti_shopping'),
    path('checkout/',zz.views.checkout,name='checkout')

]

