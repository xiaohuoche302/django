from django.db import models

# Create your models here.
class Humen(models.Model):
    name = models.CharField(
        max_length = 20,
        verbose_name='人名'
    )
    age = models.IntegerField(
        verbose_name='年纪',
        default=1
    )
    sex = models.CharField(
        max_length=6,
        verbose_name='性别'
    )
    class Meta:
        abstract = True



class Stu(Humen):
    score = models.IntegerField(
        verbose_name='成绩'
    )

class Teacher(Humen):
    salary = models.IntegerField(
        verbose_name='工资S'
    )
    def get_base_msg(self):
        msg = "姓名：{t_name},年纪:{t_age}".format(
            t_name=self.name,
            t_age=self.age)
        return msg
    def __str__(self):
        return self.name

class Movies(models.Model):
    num = models.IntegerField(
            verbose_name='集数'
    )

class Contents(models.Model):
    content = models.CharField(max_length=30,
                               verbose_name='标题')
    longtime = models.IntegerField(verbose_name='时长',
                                   default=0)
    person = models.CharField(max_length=30,
                              verbose_name='演员',
                              default=0)
    content_num = models.OneToOneField('Movies',
                                       verbose_name='集数')



