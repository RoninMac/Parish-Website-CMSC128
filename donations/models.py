"""
Donation model for tracking monetary contributions to the parish.
DATABASE TABLE: donations_donation
Related files: views.py, forms.py, admin.py, templates/donate.html
"""

from django.db import models
from django.utils import timezone


class Donation(models.Model):
    #Stores a single donation transaction

    name = models.CharField(max_length=100)
    #Donor's full name (max 100 characters)

    email = models.EmailField()
    #Donor's email (auto-validated by EmailField)

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    #Donation amount in Philippine Pesos ₱ (max: 9,999,999.99)

    message = models.TextField(blank=True)
    #Optional prayer request or message from donor

    date = models.DateTimeField(default=timezone.now)
    #Auto-filled timestamp when donation created

    def __str__(self):
        #Display as: 'Name - ₱Amount' in admin
        return f"{self.name} - ₱{self.amount}"

    class Meta:
        verbose_name = "Donation"
        verbose_name_plural = "Donations"
        ordering = ['-date']  # Newest first
