from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render,HttpResponse
import logging
# Create your views here.
from django.core.mail import send_mail, send_mass_mail
from django.template import loader

from study08.my_util import get_random_str


def send_my_email(req):
    title = "阿里offer"
    msg = "恭喜你获得酱油一瓶"
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever = [
        '1479889168@qq.com',
    ]

    send_mail(title,msg,email_from,reciever)
    return HttpResponse("ok")

def send_email_v1(req):
    title = "阿里offer"
    msg = " "
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever = [
        '1479889168@qq.com',
    ]
    #加载模板
    templates = loader.get_template('email.html')
    #渲染模板
    html_str = templates.render({'msg':'双击666'})
    #发送邮件
    send_mail(title,msg,email_from,reciever,html_message=html_str)
    return HttpResponse("ok")

def verify(req):
    if req.method =='GET':
        return render(req,'verif.html')
    else:
        param = req.POST
        email = param.get("email")
        #生成随机字符
        random_str =get_random_str()
        #拼接验证连接
        url = "http://10.3.133.7:8000/active/" + random_str
        #加载激活模板
        tmp = loader.get_template('active.html')
        #渲染
        html_str = tmp.render({'url':url})
        #准备邮件数据
        title = "阿里offer"
        msg = " "
        email_from = settings.DEFAULT_FROM_EMAIL
        reciever = [
            email,
        ]
        # 发送邮件
        send_mail(title, msg, email_from, reciever, html_message=html_str)
        cache.set(random_str,email,120)
        return HttpResponse("ok")


def send_many_email(req):
    title = "阿里offer"
    content1 = "恭喜你获得酱油一瓶"
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever1 = [
        '1479889168@qq.com',
        '609016618@qq.com'
    ]
    content2 = "well done !!!"
    # 邮件1
    msg1 = (title, content1, email_from, reciever1)
    # 邮件2
    msg2 = ("小伙子", content2, email_from, ['1479889168@qq.com', '609016618@qq.com'])
    send_mass_mail((msg1,msg2),fail_silently=True)
    return HttpResponse("OK")
def active(req,random_str):
    res = cache.get(random_str)
    if res:
        return HttpResponse(res+"激活成功")
    else:
        return HttpResponse("验证连接无效")
def test_log(req):
    logger = logging.getLogger("django")
    logger.info("下课了")
    return HttpResponse("good")

