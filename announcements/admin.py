from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ( 'subject', 'content','date_posted')
    search_fields = ('subject', 'date_posted')