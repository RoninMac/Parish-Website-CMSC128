from django.db import models


class Subscription(models.Model):
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=128)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Display email as string representation"""
		return self.email

	