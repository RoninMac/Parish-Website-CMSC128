"""
Donation model for tracking monetary contributions to the parish.
DATABASE TABLE: donations_donation
Related files: views.py, forms.py, admin.py, templates/donate.html
"""

from django.db import models
from django.utils import timezone


class DonationInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10,
        decimal_places=2, 
        null=True,     # Allows NULL in the database
        blank=True,    # Allows empty submission in forms
        default=None 
      )  # Or default=0 if you prefer 0 over NULL)
    message = models.TextField(blank=True)  # Optional message from donor
    date = models.DateTimeField(default=timezone.now)
    #Auto-filled timestamp when donation created

    def __str__(self):
        #Display as: 'Name - ₱Amount' in admin
        return f"{self.name} - ₱{self.amount}"

   
