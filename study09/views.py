from django.http import HttpResponse
from django.shortcuts import render
from .tasks import first_task, send_email
from .models import Poetry
# Create your views here.


def first_celery(req):
    # 任务函数的异步调用
    first_task.delay(4)
    send_email.delay("liuda@1000phone.com")
    return HttpResponse("ok")

def create_poetry_czn(req):
    p = Poetry()
    p.title = "锄禾"
    p.author = "啊能"
    p.content = "内容内容内容"
    p.save()
    return HttpResponse("搞定")