"""
========================================
PEOPLE MODELS - Subscription Management
========================================
Models for managing parish subscribers.

MODELS:
  - Subscription: Stores email subscriptions

DATABASE TABLE: people_subscription
========================================
"""

from django.db import models


class Subscription(models.Model):
	"""
	Email subscription model for newsletter/updates.
	
	Fields:
	  - email (EmailField, unique): Subscriber's email address
	  - created_at (DateTimeField): Timestamp when subscribed (auto-filled)

	
	USAGE:
	  Subscription.objects.create(email='example@parish.com')
	  subscriber = Subscription.objects.get(email='example@parish.com')
	  
	TODO: Add 'confirmed' boolean field for opt-in verification
	TODO: Add unsubscribe link / mechanism
	"""
	email = models.EmailField(unique=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Display email as string representation"""
		return self.email

	class Meta:
		verbose_name = "Subscription"
		verbose_name_plural = "Subscriptions"
		ordering = ['-created_at']  # Newest first
