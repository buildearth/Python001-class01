学习笔记

Django(web框架)介绍
多端展示数据
网页形式展示-web框架
表现逻辑和数据存储分开
遵循了MTV设计模式,MVC框架
模型、模板、视图进行了拆分
Diango特点
强调代码复用 DRY
安装
使用2.2.13版本(LTS长期维护的)
pip install  django==2.2.13

Diango的使用
注意:
提前写好Model Veiw 和Template
一直运行这等待别人发起连接
不能直接import导入直接用，需要提前做项目和应用程序的布局
启动
创建Django的项目
django-admin startproject Mytest
目录结构:
├── Mytest
│   ├── manage.py   # 命令行工具，整个项目的管理
│   └── Mytest
│       ├── __init__.py
│       ├── settings.py   # 项目配置文件
│       ├── urls.py
│       └── wsgi.py
└── NOTE.md
创建应用程序
python manage.py help  # 查看该工具的具体功能
python manage.py startapp index  # 创建了一个index的应用程序
目录结构:
index/
├── admin.py  # 管理后台
├── apps.py  # 当前app的配置文件
├── __init__.py
├── migrations  # 数据库迁移文件
│   └── __init__.py
├── models.py  # 模型
├── tests.py  # 自动化测试
└── views.py  # 视图
真正的启动
python manage.py runserver  #默认运行是127.0.0.1:8000的地址
可以自行配置访问地址:
python manage.py runserver 0.0.0.0:80  # 可以让局域网外部的人可以访问
Django每个文件的介绍
程序的入口是manage.py,其配置文件是卸载settings.py中.
settings.py
项目路径
BASE_DIR
密钥
SECRET_KEY
作用:
用于生产环境部署时的一个设置，防止被别人跨站入侵
建议:
建议修改一个比较长的密钥，密钥的复杂性也做修改
域名访问权限
ALLOWED_HOSTS
一般不会在这个里面进行配置，不管它
App列表
项目默认支持的应用程序
内容解析:
   {# 内置后台管理系统
    'django.contrib.admin',
   # 内置用户登录系统
    'django.contrib.auth',
   # 所有model元数据
    'django.contrib.contenttypes',
   # 会话，表示当前访问网站的用户身份
    'django.contrib.sessions',
   # 消息提示
    'django.contrib.messages',
   # 静态资源路径
    'django.contrib.staticfiles',
   # 注册自己的app
    'index',}
注意：
不要随意修改默认应用程序书写的顺序，其加载是有顺序的，从上往下依次加载应用程序
自己写的加入到最下面
静态资源，包括CSS,JavaScript,图片等
STATIC_URL
将静态文件放入到指定目录下，系统自动识别
模板文件
TEMPLATES
默认情况下不需要设置
内容:
{
# 定义模板的引擎
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
# 设置模板的路径，一般不再这里设置，在应用程序里面会放置模板
        'DIRS': [],
# 表示在app里面去查找模板文件
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
数据库配置
DATABASES
Django中默认的数据引擎是sqlite3
添加自己数据库的配置：
{
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 数据库名,
 'USER':'root',
 'PASSWORD':'pwd',
 'HOST':'127.0.0.1',
 'PORT':'3306',
    }
  # 生产环境中可能会链接第二个数据库
  'db1'{...}
}
数据配置换之后还不能直接使用：
差一个引擎功能，使用pymysql这个包,按照之后如下操作:
1.需要在 manage.py同级的项目目录下的__init__文件中导入:
            import pymysql
            pymysql.install_as_MySQLdb()

2.导入之后需要解决的问题:
1.django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.错误
找到base.py,将判断版本的代码注释掉
2.'str' object has no attribute 'decode'错误
将其位置改为encode就ok

运行时可能遇到的错误:
OSError: mysql_config not find # 找不到mysql客户端
配置环境变量: export PATH=$PATH:/usr/local/mysql/bin
缓存
中间件
MIDDLEWARE
请求和返回中间需呀做的事情
注意：
不建议(对于中间件使用不熟悉时)修改其书写顺序，请求过程是从上到下，返回过程是从下到上加载
需要修改的文件(简单开发):
urls调度器
作用：
接收用户的URL请求信息,对请求进行匹配处理
匹配路径: setting.py:ROOT_URLCONF ----> Mytest.urls中进行匹配 ----> path('', include('index.urls'))(匹配路径没有在项目中，而是在应用程序中)从settings.py中找到index app ----> 去index/urls.py中匹配 ----> path('', views.index)匹配到对于视图处理 ----> index(request)请求给到这个方法做请求的响应
url支持变量：
对类型做处理，正则匹配处，自定义函数处理
支持对URL设置变量
str
int
path('<int:year>', views.myyear)  # 传入的参数会赋值给year变量
path('<int:year>/<str:name>', views.name)  # 多个参数传入
slug
uuid
path
正则，判断输入的内容
    re_path('(?P<year>[0-9]{4})', views.myyear, name = 'urlyear')  #?P表示将输入赋值到变量year中进行匹配
    re_path('(?P<year>[0-9]{4}).html', views.myyear)  # 匹配 http://127.0.0.1:8000/1996.html，将匹配到的1996传入到myyear中

自定义过滤器(正则和变量相结合)
1.模块导入
from django.urls import register_converter
2.自定义匹配规则编写，在urls统计目录下创建converters.py文件
        class IntConverter:
            regex = '[0-9]+'

            def to_python(self, value):
                return int(value)

            def to_url(self, value):
                return str(value)

3.使用
        register_converter(converters.IntConverter, 'myint')  # 将自定义匹配规则绑定上一个名字
        path('<myint:year>', views.year)  # 根据自定义规则匹配，然后将year作为参数传入到views.year函数中

view视图
请求的一个返回
Response 是正常的返回
Render 是把Response再做了一层的封装
return render(request, 'yearview.html')  # 去应用程序的目录下查找templates文件夹下的模板,返回一个文件中的内容
Redict 处理之后跳转
models数据库
不是直接操作数据库，做了一个对象的提取，类的名称是表的名称，类中的属性是表中的字段
ORM创建数据表
Django提供了一个自动生成访问数据库的API
from django.db import models
class Person(models.Model):
    id = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
等同于SQL语句：
    create table myapp_person(
        id serial not null primary key,
        first_name varchar(30) not null,
       last_name varchar(30) nt null
    );

python manager.py makemigrations  # 对应的数据表class加上一些必要的功能
python manager.py migrate  # 转换成SQL的表
ORM操作数据表
根据属性去操作
>>> from index.models import *
>>> dir()
['Person', 'Type', '__builtins__', 'models']
>>> p = Person()
>>> p.id = 1
>>> p.first_name = 'as'
>>> p.last_name = 'xx'
>>> p.save()


使用ORM框架api
>>> Person.objects.create(id=2,first_name='lds', last_name = 'b')  # 添加一行数据
>>> Person.objects.get(id=2).first_name  # 根据id查询一行的，拿到这行的first_name
>>> Person.objects.filter(first_name='lds').update(first_name='www') # 修改first_name='lds'这行的first_name的值，返回值是修改了多少行
>>> Person.objects.filter(id=1).delete()  # 删除单条数据
>>> Person.objects.all().delete()  # 删除全部数据

其他常用查询方法:
>>> n = Person.objects.all()
>>> n[1].first_name
>>> Person.objects.values_list('first_name')  # 取first
>>> Person.objects.values_list('first_name').count()  # 使用python的函数 count()

模板
通过View视图将参数传递到模板
模板变量  {{ variables }}
从url获取模板变量  {% url 'urlyear' 2020 %}  # 将2020传递到urlyear,通过template回到url，从url再去调用视图
读取静态资源内容  {% static "css/header.css"%}
for 遍历标签 {% for type in type_list%} {% endfor %}
if 判断标签 {% if name.type == type.type %} {%endif%}
展示数据库中的内容
n = Name.objects.all()
return render(request, 'bookslist.html', locals())  # locals()将本地所有变量获取，然后传递到'bookslist.html'模板中

bookslist.html
<html>
<head>
    <meta charset='UTF-8'>
    <title>Person</title>
</head>
<body>
{% for p in n %}
    <div> id: {{p.id}}<br>
        first_name:{{p.first_name}}<br>
        last_name:{{p.last_name}}
    </div>
{%endfor%}
</body>

数据库反向创建Django的models
python manage.py inspectdb > models.py

