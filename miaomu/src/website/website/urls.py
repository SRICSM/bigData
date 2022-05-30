"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from app.views import *

urlpatterns = [
    path('', index),
    re_path('^index/$', showpic),
    # path('admin/', admin.site.urls),
    # 苗木网数据
    re_path('^yuanlin/$', yuanlin),
    # 花木网数据
    re_path('^huamu/$', huamu),
    # 苗木网json数据接口
    path('yuanlin/data/get/', get_data),
    # 花木网json数据接口
    path('huamu/data/get/', get_data),
    # 搜索接口json数据接口
    re_path('^data/search/', search_data),
    # 搜索
    re_path('^search/$', search),
    # 苗木类型统计分析
    re_path('^yuanlin/show/miaomu_types/$', miaomu_types)
]
