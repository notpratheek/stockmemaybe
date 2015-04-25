from django.db import models

class Source(models.Model):
	source = models.CharField(max_length=100)
	def __str__(self):
		return source

class Company(models.Model):
	ticker = models.CharField(max_length=10)
	def __str__(self):
		return self.ticker

class Messages(models.Model):
	company = models.ForeignKey(Company)
	source = models.ForeignKey(Source)
	created_at = models.DateTimeField('date published')
	text = models.CharField(max_length=250)
	def __str__(self):
		return self.text
