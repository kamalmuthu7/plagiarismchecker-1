
from django.db import models
from django.contrib.auth.models import User

class Data(models.Model):
	data = models.TextField()
	user = models.ForeignKey(User)
	# keywords = models.CharField(max_length=500)
