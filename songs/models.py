from django.db import models

# Create your models here.
class Songs(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    lyrics = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return f"{self.title} by {self.artist}"
