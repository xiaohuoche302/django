from __future__ import absolute_import, unicode_literals
from django.db.models.signals import pre_save,post_save

from .celery import app as celery_app
import pymysql
pymysql.install_as_MySQLdb()
def pre_save_model(sender,**kwargs):
    print(sender)
    print(kwargs)

pre_save.connect(pre_save_model)