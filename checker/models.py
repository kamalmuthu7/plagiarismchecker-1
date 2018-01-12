
from django.db import models
from django.contrib.auth.models import User
from django.core.files.base import File

class Data(models.Model):
	data = models.TextField()
	doc = models.FileField(upload_to='documents/%Y/%m/%d')
	user = models.ForeignKey(User)
	# keywords = models.CharField(max_length=500)
