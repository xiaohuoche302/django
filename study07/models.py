from django.contrib.auth.models import AbstractUser
from django.db import models
# from tinymce.models import HTMLField


class MyUser(AbstractUser):
    phone = models.CharField(
        max_length=13,
        verbose_name='手机号',
        unique=True
    )
    icon = models.ImageField(upload_to='icons',
                             null=True)

class Player(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="游戏名字"
    )
    desc = models.CharField(
        max_length=251,
        verbose_name="简介"
    )
    rate = models.FloatField(
        verbose_name="评分"
    )
    def __str__(self):
        return self.name

class Humen(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="游戏角色"
    )
    player = models.ForeignKey('Player',
                                  verbose_name="所属游戏")