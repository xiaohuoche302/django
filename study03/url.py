from django.conf.urls import url
from study03.views import *
urlpatterns = [
    url(r'^get_count/$',get_count,name='get_count'),
    url(r'^get_player/$',get_player,name='get_player'),
    url(r'^get_player_by_q/$',get_player_by_q,name='get_player_by_q'),
    url(r'^create_china_player/$',create_china_player,name='create_china_player'),
    url(r'^get_weizhi$', get_weizhi, name='get_weizhi'),
    url(r'^get_yingxiong/(\d+)$', get_yingxiong, name='get_yingxiong'),
    url(r'^get_wei_zhi$', get_wei_zhi, name='get_wei_zhi'),
    url(r'^get_ying_xiong/(\d+)$', get_ying_xiong, name='get_ying_xiong'),
    ]