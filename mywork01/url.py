from django.conf.urls import url
from mywork01.views import *

urlpatterns = [
    url(r'^home/$',home,name='home'),
    url(r'^market/$', market, name='market'),
    url(r'^cart/$', cart, name='cart'),
    url(r'^mine/$', mine, name='mine'),

]
