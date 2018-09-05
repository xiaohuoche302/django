from django.shortcuts import render,HttpResponse

# Create your views here.
from study01.models import Person


def hello(requset):
    return HttpResponse('●hhhhh')

def xxx(request):
    return render(request,'xxx.html')

def zzz(request):
    context={}
    person = Person.objects.all()
    context['person'] = person
    return render(request,'zzz.html',context)

def getinfo(request):
    nid = request.GET.get('nid')
    infolist = Person.objects.filter(id = nid)
    print(infolist)
    infolist=infolist[0]
    return render(request,'getinfo.html',{'infolist':infolist})

