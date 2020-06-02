from django.db import models

# Create your models here.

class Job(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length = 200)
	startDate = models.CharField(max_length = 20,  blank = True)
	endDate = models.CharField(max_length = 20,  blank = True)
	description = models.CharField(max_length = 200, blank = True)
	# long_description = models.TextField(blank = True)
	organization = models.CharField(max_length = 50, blank = True)
	# organization_website = models.CharField(max_length = 150, blank = True)

	def __str__(self):
		return self.organization

class Projects(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length = 200)
	github = models.CharField(max_length = 100)
	title = models.CharField(max_length = 100)

	def __str__(self):
		return self.title

class Education(models.Model):
	image = models.ImageField(upload_to='images/')
	school = models.CharField(max_length = 100)
	degree = models.CharField(max_length = 100)
	grade = models.FloatField()
	totalGrades = models.FloatField(blank = True, default = 100)

	def __str__(self):
		return self.school

class Skills(models.Model):
	skill = models.CharField(max_length = 50)
	label = models.CharField(max_length = 35, blank = True)

	def __str__(self):
		return self.skill

class Accomplishments(models.Model):
	summary = models.CharField(max_length = 100)
	title = models.CharField(max_length = 25)

	def __str__(self):
		return self.title

