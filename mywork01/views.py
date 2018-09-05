from django.shortcuts import render

# Create your views here.
def home(req):
    data={
        'title':'首页'
    }
    return render(req,'home/home.html',data)
def market(req):
    data={
        'title':'闪购'
    }
    return render(req,'home/home.html',data)
def cart(req):
    data={
        'title':'购物车'
    }
    return render(req,'home/home.html',data)
def mine(req):
    data={
        'title':'我的'
    }
    return render(req,'home/home.html',data)