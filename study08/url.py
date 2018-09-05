from django.conf.urls import url

from study08.views import *

urlpatterns = [
    url(r'^send_my_email',send_my_email,name='send_my_email'),

    url(r'^send_email_v1',send_email_v1,name='send_email_v1'),
    url(r'^verify', verify, name='verify'),
    url(r'^active/(.+)', active, name='active'),
    url(r'^send_many_email', send_many_email, name='send_many_email'),


    url(r'^test_log',test_log,name='test_log'),
]