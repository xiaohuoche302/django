from django.core.cache import cache
from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
from django.views.decorators.cache import cache_page

from study07.models import Player
from .my_util import get_random_color
import os
import io
import random
import time

# Create your views here.
def get_verify_img(req):
    #画布背景颜色
    bg_color = get_random_color()
    img_size = (150,70)
    #实例化一个画布
    image = Image.new("RGB",img_size,bg_color)
    #实例化一个画笔
    draw = ImageDraw.Draw(image,"RGB")
    #设置文本颜色
    # text_color = (255,0,0)
    #创建字体
    font_path ="/home/xiaohuoche/gz1803/xxxx/study07/static/fonts/ADOBEARABIC-BOLDITALIC.OTF"
    font = ImageFont.truetype(font_path,30)

    source = "asdfghjklqwertyuiopzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789"
    code_str =""
    for i in range(4):
        text_color = get_random_color()
        tmp_num = random.randrange(len(source))
        random_str = source[tmp_num]
        code_str += random_str
        draw.text((30 + 30*i, 20), random_str, text_color, font)
    req.session['code'] = code_str

    #使用画笔将文字画到画布指定位置
    # draw.text((30,35),"X",text_color,font)
    # draw.text((60, 35), "2", text_color, font)
    # draw.text((80, 35), "3", text_color, font)
    #获得一个缓存区
    buf = io.BytesIO()
    #将图片保存到缓存区
    image.save(buf,'png')
    #将缓存区的内容，返回给前端
    return HttpResponse(buf.getvalue(),'image/png')

def login_api(req):
    if req.method == 'GET':
        return render(req,'login_api.html')
    else:
        params = req.POST
        code = params.get("verify_code")
        print(code)
        server_code = req.session.get("code")
        print(server_code)
        if server_code.lower() == code.lower():
            return HttpResponse('ok')
        else:
            return HttpResponse('no ok')
@cache_page(60)
def get_data(req):
    time.sleep(5)
    return HttpResponse("睡醒了")



@cache_page(60)
def get_data(req):
#     假装在拼命的查数据库
    time.sleep(5)
    return HttpResponse("睡醒了")

def get_players(req):
    # 在缓存尝试拿数据
    data = cache.get("players")
    if data:
        # 如果拿到缓存数据 直接返回
        return HttpResponse(data)
    else:
        # 没拿到
        # 假装拿很久
        time.sleep(5)
        # 拿数据
        players = Player.objects.all()
        # 设置缓存
        cache.set("players", players, 30)
        # 把数据返回给前端
        return HttpResponse(players)


