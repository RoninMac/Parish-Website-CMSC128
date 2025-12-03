from django.db import models
from django.contrib.auth.models import User

class ChurchGroups(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    created_at = models.DateField()
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False)

    def __str__(self):
        return self.name
