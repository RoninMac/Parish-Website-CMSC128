from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Songs(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    lyrics = models.TextField()

    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.title} by {self.artist}"
