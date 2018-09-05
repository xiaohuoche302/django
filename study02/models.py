from django.db import models

# Create your models here.
class Hyrz(models.Model):
    name = models.CharField(max_length=40,
                            verbose_name="分类名",
                            db_column='c_name',
                            unique=True)
    desc = models.TextField(max_length=1000,
                            verbose_name="描述")
    def __str__(self):
        return self.name
    pass
    class Meta:
        db_table = "category"


class Goods(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    in_datetime = models.DateTimeField(auto_now_add=True,
                                       verbose_name="生产日期")
    category = models.ForeignKey('Hyrz',
                                 verbose_name="分类")
    def __str__(self):
        return self.name


class IdCard(models.Model):
    num = models.CharField(max_length=18,
                           verbose_name="身份证号")
    unite = models.CharField(max_length=30,
                             verbose_name="签发单位")

class Person(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name="名字")
    sex = models.CharField(max_length=10,
                           verbose_name="性别")
    idcard = models.OneToOneField('IdCard',
                                  verbose_name="身份证")

class Author(models.Model):
    name = models.CharField(max_length=20)


class Book(models.Model):
    title = models.CharField(max_length=20)
    authors = models.ManyToManyField('Author')