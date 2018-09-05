from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse, redirect

# Create your views here.
def copy(req):
    return render(req,'work.html')

def response_index(req):
    response = HttpResponse()
    response.content = "content"
    response.write("write")
    response.flush()
    response.status_code =404
    return response

def get_json(req):
    data = [1,2,34]
    return JsonResponse({'data':data})

def register(req):
    if req.method =="GET":
        return render(req,"register.html")
    else:
        params = req.POST
        u_name = params.get("u_name")
        pwd = params.get("pwd")
        confirm_pwd = params.get("confirm_pwd")
        #判断用户的输入是否满足基本要求
        if u_name and len(u_name)>6 and pwd and confirm_pwd and pwd == confirm_pwd:
            # 判断用户是否已经被注册
            exists_flag = User.objects.filter(username=u_name).exists()
            if exists_flag :
                return HttpResponse("该用户被注册")
            else:
                #如果没有被注册，那么就创建用户
                user = User.objects.create_user(username=u_name,password=pwd)
                return HttpResponse("创建了"+ user.username)
        else:
            return HttpResponse("账号密码格式错误")

def my_login_v1(req):
    if req.method == 'GET':
        return render(req,'my_login.html')
    else:
        #拿参数
        params = req.POST
        u_name = params.get("u_name")
        pwd = params.get("pwd")
        #校验数据格式
        if u_name and len(u_name)>3 and pwd and len(pwd)>3:
            user = authenticate(username = u_name,password = pwd)
            if user:
                login(req,user)
                return HttpResponse("OK")
            else:
                return HttpResponse("账号密码错误")
        else:
            return HttpResponse("请补全信息")

def new_index(req):
    user = req.user
    return render(req,'new_index.html',{'u_name':user.username})

def new_logout(req):
    logout(req)
    return redirect('new_index')

