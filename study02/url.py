from django.conf.urls import url
from study02.views import cates,test,cate_filter,cates_filter_in,get_goods_by_datetime,person,idcard

urlpatterns = [
    url(r'^res/$',cates),
    url(r'^test/$',test),
    url(r'^kw/$',cate_filter),
    url(r'^kwi/$',cates_filter_in),
    url(r'^time/$',get_goods_by_datetime),
    url(r'^person/(\d+)/$',person,name='person'),
    url(r'^idcard/$',idcard,name='idcard'),
]