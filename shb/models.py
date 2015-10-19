from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Newman(models.Model):
	newman_name = models.CharField(max_length=200)
	newman_instrument = models.CharField(max_length=100)
	owner = models.ForeignKey('Oldmen', null=True, blank=True)
	points = models.IntegerField(default=0)
	def __str__(self):
		return self.newman_name
	def calc_points(self):
		self.points = 0
		for shb in self.shb_set.all():
			if shb.limited:
				self.points += 7
			else:
				self.points += 5
		self.save()
		return self.points
	calc_points.admin_order_field = 'points'
	calc_points.short_description = "Point Total"


class Oldmen(models.Model):
	team_name =models.CharField(max_length=200)
	team_owner = models.CharField(max_length=200)
	team_points = models.IntegerField(default=0)
	def __str__(self):
		return self.team_owner
	def team_total(self):
		self.team_points = 0
		for n in self.newman_set.all():
			self.team_points += n.points
			self.save()
		return self.team_points
class SHB(models.Model):
	shb_name = models.CharField(max_length=200)
	shb_time = models.DateTimeField('Date of SHB')
	newman_list = models.ManyToManyField('Newman')
	limited = models.BooleanField(default=False)
	def __str__(self):
		return self.shb_name