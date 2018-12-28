from django.shortcuts import render
from django.shortcuts import HttpResponse  # 导入这个模块
from web_demo import models
# Create your views here.

user_list = []  # 顶部增加一个新列表


def index(request):
    """
    第一个参数必须为request,名字可以改，但最好不要，这是潜规则，
    request里封装了用户请求的所有内容
    """
    # 不直接返回字符串，必须由HttpResponse这个类封装起来，才能被HTTP协议识别
    # return HttpResponse('hello world')
    # render方法使用数字字典和请求元数据，渲染一个指定的HTML模板，其中有多个参数，第一个参数必须为request,第二个是模板
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "web" and password == "123456":
            # print(username, password)
            # temp = {'user': username, 'pwd': password}  # 将发送过来的用户名和密码构造成一个字典
            # user_list.append(temp)  # 将temp添加到user_list
            # 将数据保存到数据库
            models.UserInfo.objects.create(user=username, pwd=password)

    # 从数据库中读取所有数据，注意缩进
    user_list = models.UserInfo.objects.all()
    # 将用户列表作为上下文参数供render渲染index页面
    return render(request, 'index.html', {'data': user_list})
