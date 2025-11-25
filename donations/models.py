from django.db import models

from django.utils import timezone

class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - ₱{self.amount}"
