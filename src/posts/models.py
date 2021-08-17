from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	#author = models.CharField(max_length=120)       (not working yet)
    #Timestamp
	def __str__(self):
		return self.title