from django.db import models
import random

# Create your models here.
class Team(models.Model):
	name = models.CharField(max_length=30,
							verbose_name="球队名",
							db_index=True)

	contry = models.CharField(max_length=30,
								verbose_name="所属国家")
	def __str__(self):
		return self.name

class PlayerManager(models.Manager):
	def create_china_play(self):
		player = Player()
		print(player)
		player.name = "西罗"+str(random.randint(0,100))
		player.age = random.randrange(100)
		player.count = random.randrange(1000)
		player.team_id = 1
		player.save()
		return player


class Player(models.Model):
	name = models.CharField(max_length=30,
							verbose_name='名字')

	age = models.IntegerField(verbose_name="年龄")

	count = models.IntegerField(verbose_name='火力输出')

	team = models.ForeignKey('Team',verbose_name='所属球队',
							null = True)
	objects = models.Manager()
	my_objects_one = PlayerManager()
	def __str__(self):
		return self.name

class WeiZhi(models.Model):
	weizhi = models.CharField(max_length=30)


class YingXiong(models.Model):
	name = models.CharField(max_length=30)

	wei_zhi = models.ForeignKey('WeiZhi')

class Wei_zhi(models.Model):
	weizhi = models.CharField(max_length=30)
	ying_xiong = models.ForeignKey('Ying_Xiong')

class Ying_Xiong(models.Model):
	name = models.CharField(max_length=30)
	def __str__(self):
		return self.name