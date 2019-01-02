升级pip3:python -m pip install --upgrade pip
django-admin help
目录说明: 
    项目名称：demo_web
    __init__.py 空文件
    settings.py 主配置文件
    urls.py 主路由
    wsgi.py 网关接口
    templates目录是HTML文件存放处
    manage.py是Django项目管理文件。


python manage.py startapp web_demo  创建了一个叫做web_demo的APP

编写路由:demo_web下的urls.py文件
1.先导入对应app中的视图文件 from web_demo import views

2.添加路由，重点是路由表达式和后边的视图函数  path('index/', views.index, name='index')
3.编写视图函数，路由转发用户请求到视图函数。视图函数处理用户请求，也就是编写业务处理逻辑，一般都在views.py文件里
views.py文件备注

4. 运行服务 python manage.py runserver 127.0.0.1:8000 服务就启动了
5.在templates中建一个index.html文件
6.替换urls 文件中的HttpReponse为Render方法
7.为了让django知道我们的HTML文件在哪里，需要修改settings文件的相应内容。但默认情况下。它正好适用，你无需修改
8. 前端三大块HTML、CSS、JavaScript，还有各种插件，使用齐全才是一个完整的页面
创建statics目录，加入js文件
在Django中，一般将这些静态文件放在statics目录中。
在settings中配置静态目录STATICFILES_DIRS
9.在templates目录下的index.html中引入js
10.在index.html中加入登录用户密码输入框，修改views文件响应
11.因为django有一个跨站请求保护机制，这需要我们在index.html文件中加入一行{% csrf_token %}
成功收到了浏览器传来的信息
12.收到了用户的数据，但返回给用户的依然是个静态页面。通常我们会根据用户的数据，进行处理后再返回给用户。
修改index接收用户数据并显示
13.使用数据库
1）先注册app 在settings中INSTALLED_APPS里增加app名 web_demo
2)配置数据库表：在settings中DATABASES配置所使用的数据库
3）再编辑web_demo中的models.py文件
14.Teminal中通过命令创建数据库的表
python manage.py makemigrations

这里会有错误，
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
Did you install mysqlclient?
解决方法：pip install pymysql
出错：django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named 'MySQLdb'
在__init__.py文件中加入
import pymysql
pymysql.install_as_MySQLdb()

成功在web_demo目录中的migrations目录中生成一个0001_initial.py迁移记录文件

python manage.py migrate

这样，我们就在数据库中将所有app的数据表都创建好了,可以看到项目根目录下出现了一个db.sqlite3文件

15.现在，我们来修改views.py中的业务逻辑