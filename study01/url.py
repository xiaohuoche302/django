from django.conf.urls import url
from study01.views import hello,xxx,zzz,getinfo

urlpatterns = [
    url(r'^hello/$',hello),
    url(r'^xxx/$',xxx),
    url(r'^zzz/$',zzz),
    url(r'getinfo.html/',getinfo)

]
