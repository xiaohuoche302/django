from django.conf.urls import url

from testwork.views import get_person,get_bankcard,get_to_class,get_to_student,get_to_book,get_to_authors,get_to_name,get_to_title

urlpatterns = [

    url(r'^get_person/(\d+)/$',get_person,name='get_person'),
    url(r'^get_bankcard/$',get_bankcard,name='get_bankcard'),
    url(r'^get_to_class/$', get_to_class, name='get_to_class'),
    url(r'^get_to_student/(\d+)$', get_to_student, name='get_to_student'),
    url(r'^get_to_book/$', get_to_book, name='get_to_book'),
    url(r'^get_to_authors/(\d+)$', get_to_authors, name='get_to_authors'),
    url(r'^get_to_title/(\d+)$', get_to_title, name='get_to_title'),
    url(r'^get_to_name/$', get_to_name, name='get_to_name'),
]