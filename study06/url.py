from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^copy/$', copy, name='copy'),
    url(r'^register/$', register, name='register'),
    url(r'^my_login_v1/$', my_login_v1, name='my_login_v1'),
    url(r'^new_index/$', new_index, name='new_index'),
    url(r'^new_logout/$', new_logout, name='new_logout'),

    ]