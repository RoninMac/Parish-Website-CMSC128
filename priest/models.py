from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Priest(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    bio = models.TextField()
    photo = models.ImageField(upload_to='priests/', null=True, blank=True)
    posted_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True, editable=False)

    def __str__(self):
        return self.name