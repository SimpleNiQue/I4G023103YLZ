from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	"""A modael for Posts"""
	title = models.CharField(max_length=200)
	text = models.TextField()
	author =models.ForeignKey(User, on_delete=models.CASCADE)

	created_date = models.DateTimeField(auto_now_add=True)
	published_date = models.DateTimeField(auto_now_add=True) 
