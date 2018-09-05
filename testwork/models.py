from django.db import models

# Create your models here.
#一对一关系模型
class BankCard(models.Model):
    num = models.IntegerField(verbose_name='卡号')
    bank_name = models.CharField(max_length=30,
                                 verbose_name='银行名字')
    def __str__(self):
        return self.bank_name


class Person(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='人名')
    age = models.IntegerField(verbose_name='年龄')
    bankcard = models.OneToOneField('BankCard',
                                    verbose_name='银行卡')
    def __str__(self):
        return self.name




# 定义班级


class Class(models.Model):
    class_name = models.CharField(max_length=32,
                                  verbose_name='班级名字')

    boy_num = models.IntegerField(verbose_name='男生人数')

    girl_num = models.IntegerField(verbose_name='女生人数')

    description = models.CharField(max_length=200,verbose_name='介绍')

    def __str__(self):
        return self.class_name


class Student(models.Model):
    name = models.CharField(max_length=32)

    gender = models.CharField(max_length=10, default='男')

    age = models.IntegerField()

    klass = models.ForeignKey('Class')

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='作者')

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=20,
                             verbose_name='书名')
    authors = models.ManyToManyField('Author')


    def __str__(self):
        return self.title