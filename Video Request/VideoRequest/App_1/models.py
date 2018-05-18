from django.db import models
from django.utils import timezone

# Create your models here.

class video(models.Model):
	title = models.CharField(max_length=30)

	description = models.TextField()

	date_added = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return 'Name: {}, ID: {}'.format(self.title,self.id)

	
	