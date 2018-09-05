from django.shortcuts import render,HttpResponse
from .models import Hyrz,Goods,Person,IdCard
# Create your views here.

def cates(req):
    res = Hyrz.objects.all()
    res = Hyrz.objects.filter(id = 1)
    res = Hyrz.objects.exclude(id = 1)
    res = Hyrz.objects.all().order_by("-id")
    return render(req,'res.html',{'res':res,'title':'标题'})

def test(req):
    test = req.GET.get("test")
    ress = Hyrz.objects.get(id = test)
    print(ress)
    return HttpResponse(ress)

def cate_filter(req):
    #拿参数
    key_world = req.GET.get("kw")
    #查数据库 __contains类似于sql里面的like
    res = Hyrz.objects.filter(name__contains=key_world)
    res = Hyrz.objects.filter(desc__endswith=key_world)
    print(res)
    return HttpResponse(res)

def cates_filter_in(req):
    res = Hyrz.objects.filter(pk__in = [1,3])
    return HttpResponse(res)

def get_goods_by_datetime(req):
    my_time = req.GET.get("time")
    res = Goods.objects.filter(in_datetime__year=my_time)
    return HttpResponse(res)

def idcard(request):
    idcard = IdCard.objects.all()
    content = {}
    content['idcard'] = idcard
    return render(request,'idcard.html',content)

def person(request,i_id):
    person = Person.objects.filter(idcard_id = i_id)
    return render(request,'person.html',locals())