from django.conf.urls import url
from calc.views import add,home,grade,grade_one,student

urlpatterns = [
    url(r'^add/(\d+)/(\d+)/$',add,name='add'),
    url(r'^home/$',home,name='home'),
    url(r'^grade/$',grade,name='grade'),
    url(r'^grade_one/(\d+)$',grade_one,name='grade_one'),
    url(r'^student/(\d+)$',student,name='student'),

]