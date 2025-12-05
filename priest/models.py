from django.db import models

# Create your models here.
class Priest(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    bio = models.TextField()
    photo = models.ImageField(upload_to='priests/', null=True, blank=True)

    def __str__(self):
        return self.name