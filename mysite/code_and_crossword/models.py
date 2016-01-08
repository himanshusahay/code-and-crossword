from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.

class Leaderboard(models.Model):
	name = models.CharField(max_length = 20)
	sub_date = models.DateTimeField('submission date')
	score = models.IntegerField()
	code_score = models.IntegerField()
	crossword_score = models.IntegerField()

class Code(models.Model):
	question = models.CharField(max_length = 1000)
	level = models.IntegerField()

	def __str__(self):
		return self.question + ". level = " + str(self.level)

class Code_Answer(forms.Form):
	answer = forms.CharField(max_length = 1000)

class Crossword(models.Model):
	question = models.CharField(max_length = 3000)
	level = models.IntegerField()

	def __str__(self):
		return self.question + ". level = " + str(self.level)

class Crossword_Answer(forms.Form):
	answer = forms.CharField(max_length = 3000)
