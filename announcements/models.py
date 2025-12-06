from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Announcement(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='announcements/', null=True, blank=True)
    
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False)

    def __str__(self):
        return self.subject