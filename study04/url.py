from django.conf.urls import url
from .views import *
urlpatterns = [
	url(r'^get_person_by_bank/$',get_person_by_bank,name='get_person_by_bank'),
    url(r'^get_engineer_by_desc/$',get_engineer_by_desc,name='get_engineer_by_desc'),
    url(r'^get_engineer_by_language/$',get_engineer_by_language,name='get_engineer_by_language'),
    url(r'^get_author_by_book/$', get_author_by_book, name='get_author_by_book'),
    url(r'^get_book_by_author/$', get_book_by_author, name='get_book_by_author'),
    url(r'^remove_person/$', remove_person, name='remove_person'),
    url(r'^remove_bank/$', remove_bank, name='bank'),


    ]