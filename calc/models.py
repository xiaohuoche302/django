from django.db import models

# Create your models here.
class Grade(models.Model):

	gname = models.CharField(max_length=10,
		verbose_name="班级名称" )

	gdate = models.DateTimeField(verbose_name="开班日期")

	ggirlnum = models.IntegerField(verbose_name="女生数量")

	gboynum = models.IntegerField(verbose_name="男生数量")

	isDelete = models.BooleanField(default=False,
		verbose_name="是否已逻辑删除该班级")

	def __str__(self):
		return self.gname


class Students(models.Model):
	sname = models.CharField(max_length=20,
		verbose_name="学生姓名")

	sgender = models.BooleanField(default=True,
		verbose_name="学生性别")

	sage = models.IntegerField(verbose_name="学生年龄")

	sinfo = models.CharField(max_length=20,
		verbose_name="备注信息")

	isDelete = models.BooleanField(default=False,
		verbose_name="是否逻辑删除学生")

	sgrade = models.ForeignKey(Grade)

	def __str__(self):
		return self.sname

