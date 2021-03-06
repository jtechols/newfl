from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Newman(models.Model):
	newman_name = models.CharField(max_length=200)
	newman_instrument = models.CharField(max_length=100)
	owner = models.ForeignKey('Oldmen', null=True, blank=True)
	points = models.IntegerField(default=0)
	career_points = models.IntegerField(default=0)
	imgFileName = models.CharField(max_length=200, null=True)
	woodwind = models.BooleanField(default=False)
	saxophone = models.BooleanField(default=False)
	lowbrass = models.BooleanField(default=False)
	highbrass = models.BooleanField(default=False)
	perc = models.BooleanField(default=False)
	bench = models.BooleanField(default=False)
	flex = models.BooleanField(default=False)
	def __str__(self):
		return self.newman_name
	def calc_points(self):
		self.points = 0
		for shb in self.shb_set.filter(active=True):
			if shb.limited:
				self.points += 7
			else:
				self.points += 5
		self.save()
		return self.points
	calc_points.admin_order_field = 'points'
	calc_points.short_description = "Point Total"
	def section(self):
		wwind = ["Picc", "Net 1", "Net 2"] 
		sax = ["Alto 1", "Alto 2", "Tenor"]
		upbrass = ["Trumpet 1", "Trumpet 2", "Mello"]
		lwbrass = ["Bone 1", "Bone 2", "Bearitone", "Bass"]
		perc = ["Snare", "Bass Drum", "Tenor Drums", "Cymbals", "Glock"]
		if self.newman_instrument in wwind:
			self.woodwind = True
			self.saxophone = False
			self.lowbrass = False
			self.highbrass = False
			self.perc = False
		if self.newman_instrument in sax:
			self.saxophone = True
			self.woodwind = False
			self.lowbrass = False
			self.highbrass = False
			self.perc = False
		if self.newman_instrument in lwbrass:
			self.lowbrass = True
			self.woodwind = False
			self.saxophone = False
			self.highbrass = False
			self.perc = False
		if self.newman_instrument in upbrass:
			self.highbrass = True
			self.woodwind = False
			self.saxophone = False
			self.lowbrass = False
			self.perc = False
		if self.newman_instrument in perc:
			self.perc = True
			self.woodwind = False
			self.saxophone = False
			self.lowbrass = False
			self.highbrass = False
		self.save()


class Oldmen(models.Model):
	team_name =models.CharField(max_length=200)
	team_owner = models.CharField(max_length=200)
	current_points = models.IntegerField(default=0)
	team_points = models.IntegerField(default=0)
	locked = models.BooleanField(default=False)
	def __str__(self):
		return self.team_owner
	def current_total(self):
		self.current_points = 0
		for n in self.newman_set.filter(bench=False):
			self.current_points += n.calc_points()
			self.save()
		return self.current_points
	def bank_points(self):
		self.team_points += self.current_points
		self.save()
		## Stores current point total in team total and then resets newman points to 0 ##
		for n in self.newman_set.all():
			n.career_points += n.points
			n.points = 0
			n.save()
		## Sets completed SHB's to inactive and upcoming SHB's to active ##
		for shb in SHB.objects.all():
			shb.set_active()

	def add_newman(self, newman_id):
		newman = Newman.objects.filter(id=newman_id)[0]
		if not person.locked:
			if len(self.newman_set.all()) < 8 and not newman.owner:
				if not self.newman_set.filter(woodwind=True, bench=False) and newman.woodwind: 
					newman.owner = self
				elif not self.newman_set.filter(saxophone=True, bench=False) and newman.saxophone: 
					newman.owner = self
				elif not self.newman_set.filter(highbrass=True, bench=False) and newman.highbrass: 
					newman.owner = self
				elif not self.newman_set.filter(lowbrass=True, bench=False) and newman.lowbrass: 
					newman.owner = self
				elif not self.newman_set.filter(perc=True, bench=False) and newman.perc: 
					newman.owner = self
				else:
					newman.owner = self
					newman.bench = True
		self.save()
		newman.save()
	def remove_newman(self, newman_id):
		newman = self.newman_set.filter(id=newman_id)[0]
		if not person.locked:
			newman.owner = None
			newman.bench = False
		self.save()
		newman.save()
	def bench_newman(self, newman_id):
		newman = self.newman_set.filter(id=newman_id)[0]
		if not person.locked:
			newman.bench = True
			newman.flex = False
		self.save()
		newman.save()
	def start_newman(self, newman_id):
		newman = self.newman_set.filter(id=newman_id)[0]
		if not self.locked:
			if not self.newman_set.filter(woodwind=True, bench=False, flex=False) and newman.woodwind: 
					newman.bench = False
					newman.flex = False
			elif not self.newman_set.filter(saxophone=True, bench=False, flex=False) and newman.saxophone: 
					newman.bench = False
					newman.flex = False
			elif not self.newman_set.filter(highbrass=True, bench=False, flex=False) and newman.highbrass: 
					newman.bench = False
					newman.flex = False
			elif not self.newman_set.filter(lowbrass=True, bench=False, flex=False) and newman.lowbrass: 
					newman.bench = False
					newman.flex = False
			elif not self.newman_set.filter(perc=True, bench=False, flex=False) and newman.perc: 
					newman.bench = False
					newman.flex = False
		self.save()
		newman.save()
	def flex_newman(self, newman_id):
		newman = self.newman_set.filter(id=newman_id)[0]
		if not self.locked:
			if not self.newman_set.filter(flex=True):
				newman.flex = True
				newman.bench = False
		newman.save()
		self.save()
class SHB(models.Model):
	shb_name = models.CharField(max_length=200)
	shb_time = models.DateTimeField('Date of SHB')
	newman_list = models.ManyToManyField('Newman')
	limited = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	def __str__(self):
		return self.shb_name
	def set_active(self):
		current_month = datetime.datetime.now().month
		current_day = datetime.datetime.now().day
		if current_month < self.shb_time.month:
			self.active = True
		elif current_month > self.shb_time.month:
			self.active = False
		elif current_month == self.shb_time.month:
			if current_day < self.shb_time.day:
				self.active = True
			else:
				self.active = False
		else:
			self.active = False
		self.save()

