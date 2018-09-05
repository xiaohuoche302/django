from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse, redirect
from study08.my_util import get_random_str
from django.core.cache import cache
import random
import uuid
import hashlib
from study07.models import MyUser
from .models import Movies,Contents
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail,send_mass_mail

# Create your views here.

def get_str():
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode("utf-8")
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()

def my_index(req):
    user = req.user
    return render(req,'index.html',{'u_name':user.username})

def get_movies(req):
    get_movies = Movies.objects.all()
    return render(req,'get_movies.html',locals())
# def get_user_by_num(req, page_num):
#     page_num = int(page_num)
#     # 获得全部用户
#     users = Movies.objects.all()
#     # 创建分页
#     paginator = Paginator(
#         users,
#         USER_PEER_PAGE_NUM
#     )
#     # 参数校验
#     if page_num <= 0 or page_num > paginator.num_pages:
#         return HttpResponse("没数据了")
#     # 拿到用户指定页面的那页数据
#     page = paginator.page(page_num)
#     # 返回给用户数据
#     data = {
#         'users': page.object_list
#     }
#     print(data)
#     return render(req, 'get_user_by_num.html', data)

def get_content(req,m_id):
    get_content = Contents.objects.get(id = m_id)
    return render(req,'get_conten.html',locals())


def register(req):
    if req.method =="GET":
        return render(req,"register.html")
    else:
        params = req.POST
        u_name = params.get("u_name")
        u_email = params.get("u_email")
        u_phone = params.get("u_phone")
        pwd = params.get("pwd")
        confirm_pwd = params.get("confirm_pwd")
        icon = req.FILES['u_icon']
        random_str = get_random_str()
        #判断用户的输入是否满足基本要求
        if u_name and len(u_name)>6 and pwd and confirm_pwd and pwd == confirm_pwd:
            # 判断用户是否已经被注册
            exists_flag = MyUser.objects.filter(username=u_name).exists()
            if exists_flag :
                return HttpResponse("该用户被注册")
            else:
                #如果没有被注册，那么就创建用户
                user = MyUser.objects.create_user(username=u_name,email=u_email,password=pwd,phone=u_phone)
                # 生成随机字符
                random_str = get_str()
                # 拼接验证连接
                url = "http://10.3.133.35:8000/homework/active/" + random_str
                # 加载激活模板
                tmp = loader.get_template('active.html')
                # 渲染
                html_str = tmp.render({'url': url})
                print(html_str)

                # 准备邮箱数据
                title = "邮箱验证"
                msg = ""
                email_from = settings.DEFAULT_FROM_EMAIL
                reciever = [
                    u_email,
                ]
                send_mail(title, msg, email_from, reciever, html_message=html_str)
                cache.set(random_str, u_email, 120)
                user.icon = icon
                user.save()
                return render(req,'my_login.html')
        else:
            return HttpResponse("账号密码格式错误")
def active(req,random_str):
    res = cache.get(random_str)
    print(res)
    if res:
        #通过邮箱找到对应用户
        #给用户的状态字段做更新，从未激活太编程激活状态
        return HttpResponse(res + "激活成功")
    else:
        return HttpResponse("验证连接无效")
def my_login_v1(req):
    if req.method == 'GET':
        return render(req,'my_login.html')
    else:
        #拿参数
        params = req.POST
        u_name = params.get("u_name")
        pwd = params.get("pwd")
        code = params.get("verify_code")
        server_code = req.session.get("code")
        print(code,server_code)
        #校验数据格式
        if u_name and len(u_name)>3 and pwd and len(pwd)>3:
            user = authenticate(username = u_name,password = pwd)
            # print(user)
            if user:
                if server_code.lower() == code.lower():
                    login(req,user)
                    user_now = req.user
                    return  render(req,'index.html',{'u_name':user_now.username})
            else:
                return HttpResponse("账号密码错误或未注册")
        else:
            return HttpResponse("请补全信息")

def new_index(req):
    user = req.user
    u_icon = "http://{host}/static/uploads/{icon_url}".format(
        host=req.get_host(),
        icon_url=user.icon.url
    )
    print(u_icon)
    return render(req,'new_index.html',{'u_name':user.username,'icon':u_icon})

def new_logout(req):
    logout(req)
    return HttpResponse("退出成功")
    # return redirect('new_index')