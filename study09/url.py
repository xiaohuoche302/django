from django.conf.urls import url

from study09.views import create_poetry_czn,first_celery

urlpatterns = [

    url(r'^create_poetry_cz',create_poetry_czn,name='create_poetry_cz'),
    url(r'^first_celery',first_celery,name='first_celery'),
]