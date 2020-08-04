from django.contrib import admin
from django.urls import path, include, re_path, register_converter

from . import views, converters

register_converter(converters.IntConverter, 'myint')

urlpatterns = [
    path('', views.index),

    # 带变量的URL
    # path('<int:year>', views.year),  # 只接收整数，其他返回404
    # path('<int:year>/<str:name>', views.name)

    # 正则
    # re_path('(?P<year>[0-9]{4}).html', views.myyear, name = 'urlyear')  # 匹配 http://127.0.0.1:8000/1996.html

    # 自定义匹配规则
    path('<myint:year>', views.year),
    path('person', views.person),
]
