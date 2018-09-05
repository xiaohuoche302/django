from django.forms import model_to_dict
from django.shortcuts import render,HttpResponse
from .models import Team,Player,WeiZhi,YingXiong,Wei_zhi,Ying_Xiong
from django.db.models import Sum,F,Q
import json

# Create your views here.

def get_count(request):
	#拿全部数据
	players = Player.objects.all()
	#求火力输出总和
	res = players.aggregate(Sum('count'))
	print(res)
	return HttpResponse(res.get('count__sum'))


def get_player(req):
	#需求：年纪大于火力输出的数据
	res = Player.objects.filter(age__lt = F('count'))
	#将查询出来的对象 全部转换成数组嵌套字段的格式
	result = [model_to_dict(i) for i in res]
	print(result,type(result))
	# return HttpResponse(json.dumps(result))
	return HttpResponse(res)

def get_player_by_q(req):
	#需求: 查询年纪大于  火力输出大于  
	res = Player.objects.filter(Q(age__gt=30) | Q(count__gt=100))
	res = Player.objects.filter(Q(age__lt=30) & Q(count__lt=50))
	return HttpResponse(res)

def create_china_player(req):
	player = Player.my_objects_one.create_china_play()
	return HttpResponse("创建了一个叫{name}的男人".format(name=player.name))

def get_weizhi(req):
	weizhi = WeiZhi.objects.all()
	data = {'weizhi':weizhi}
	return render(req,'get_weizhi.html',data)

def get_yingxiong(req,weizhi_id):
	weizhi = WeiZhi.objects.get(id=weizhi_id)
	yingxiong = weizhi.yingxiong_set.all()
	data={'yingxiong':yingxiong}
	return render(req,'get_yingxiong.html',data)

def get_wei_zhi(req):
	weizhi = Wei_zhi.objects.all()
	data = {'weizhi':weizhi}
	return render(req,'get_wei_zhi.html',data)

def get_ying_xiong(req,w_id):
	weizhi = Wei_zhi.objects.get(id=w_id)
	yingxiong = weizhi.ying_xiong
	data={'yingxiong':yingxiong}
	return render(req,'get_ying_xiong.html',data)
