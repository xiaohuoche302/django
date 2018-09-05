from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^my_index/$', my_index, name='my_index'),
    url(r'^register/$', register, name='register'),
    url(r'^my_login_v1/$', my_login_v1, name='my_login_v1'),
    url(r'^new_index/$', new_index, name='new_index'),
    url(r'^new_logout/$', new_logout, name='new_logout'),
    url(r'^get_movies/$', get_movies, name='get_movies'),
    url(r'^get_content/(\d+)$', get_content, name='get_content'),
    url(r'^active/(.+)', active, name='active'),

]